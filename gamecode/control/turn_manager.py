from gamecode.control.jail_manager import JailManager
from gamecode.gameplay.dice import Dice


class TurnError(Exception):
    pass


class TurnManager:
    def __init__(self, game):
        self.game = game
        self.dice = Dice()
        self.can_roll = True
        self.current_player_id = 0
        self.jail_mgr = JailManager(self, self.game.get_tile("Jail"))

    def roll(self):
        if not self.can_roll:
            raise TurnError("No more throws left this turn!")
        elif not self.current_tile_owned():
            raise TurnError("You need to buy or auction the tile first!")
        else:
            self.dice.roll()
            current_player = self.get_current_player()
            if self.dice.repeats < 3:
                current_player.start_from(self.get_current_tile(), self.dice)
                current_player.land_on(self.get_current_tile(), self.dice)
            else:
                self.jail_mgr.put_in_jail(self.get_current_player())
            self.can_roll = self.dice.same() and not current_player.in_jail

    def next(self):
        if self.can_roll:
            raise TurnError("You must roll first!")
        elif not self.current_tile_owned():
            raise TurnError("You must either auction or buy this tile!")
        else:
            if not self.get_current_player().positive_balance():
                self.game.players.kill(self.get_current_player())
            self.current_player_id += 1
            self.current_player_id %= self.game.get_player_count()
            if self.game.get_player_count() == 1:
                self.game.end(self.get_current_player())
                return
            self.can_roll = True
            self.dice = Dice()

    def use_card(self):
        self.jail_mgr.use_card()

    def buy_out(self):
        self.jail_mgr.buy_out()

    def current_tile_owned(self):
        try:
            return self.get_current_tile().owned()
        except AttributeError:
            return True

    def get_current_tile(self):
        return self.game.get_tile(self.get_current_player().position)

    def get_current_player(self):
        return self.game.get_player(self.current_player_id)

    def info_dice(self):
        print(self.dice)

    def info_current_player(self):
        print(self.get_current_player())
