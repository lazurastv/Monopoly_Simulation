from game.control.jail_manager import JailManager
from game.gameplay.dice import Dice


class TurnManager:
    def __init__(self, info, game):
        self.info = info
        self.game = game
        self.dice = Dice()
        self.can_throw = True
        self.current_player_id = 0
        self.jail_mgr = JailManager(self, self.info.get_tile("Jail"))

    def roll(self):
        if not self.can_throw:
            print("No more throws left this turn!")
        elif not self.current_tile_owned():
            print("You need to buy or auction the tile first!")
        else:
            self.dice.throw()
            current_player = self.get_current_player()
            if self.dice.repeats < 3:
                current_player.start_from(self.get_current_tile(), self.dice)
                current_player.land_on(self.get_current_tile(), self.dice)
            else:
                self.jail_mgr.put_in_jail(self.get_current_player())
            self.can_throw = self.dice.same() and current_player not in self.info.get_tile("Jail")

    def next(self):
        if self.can_throw:
            print("You must throw first!")
        elif not self.current_tile_owned():
            print("You must either auction or buy this tile!")
        else:
            if not self.get_current_player().positive_balance():
                self.game.players.kill(self.get_current_player())
            self.current_player_id += 1
            self.current_player_id %= self.info.get_player_count()
            self.can_throw = True
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
        return self.info.get_tile(self.get_current_player().position)

    def get_current_player(self):
        return self.info.get_player(self.current_player_id)

    def info_dice(self):
        print(self.dice)

    def info_current_player(self):
        print(self.get_current_player())
