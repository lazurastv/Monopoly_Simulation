from copy import deepcopy

from gamecode.control.jail_manager import JailManager
from gamecode.gameplay.dice import Dice


class MustRollError(Exception):
    def __init__(self):
        super().__init__("You must roll the dice before ending your turn!")


class NoThrowsLeftError(Exception):
    def __init__(self):
        super().__init__("You have no more throws left!")


class TileNotOwnedError(Exception):
    def __init__(self):
        super().__init__("The current tile must have an owner!")


class TurnManager:
    def __init__(self, game):
        self.game = game
        self.dice = Dice()
        self.can_roll = True
        self.current_player_index = 0
        self.jail_mgr = JailManager(self)

    def copy(self, game):
        turn_copy = TurnManager(game)
        turn_copy.dice = deepcopy(self.dice)
        turn_copy.can_roll = self.can_roll
        turn_copy.current_player_index = self.current_player_index
        return turn_copy

    def roll(self):
        if not self.can_roll:
            raise NoThrowsLeftError
        elif not self.current_tile_owned() and self.dice.repeats > 0:
            raise TileNotOwnedError
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
            raise MustRollError
        elif not self.current_tile_owned():
            raise TileNotOwnedError
        else:
            if not self.get_current_player().positive_balance():
                self.game.players.kill(self.get_current_player())
            self.current_player_index += 1
            self.current_player_index %= self.game.get_player_count()
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
        return self.game.get_player(self.current_player_index)

    def info_dice(self):
        print(self.dice)

    def info_current_player(self):
        print(self.get_current_player())
