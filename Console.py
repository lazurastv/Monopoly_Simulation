from Dice import Dice
from Tiles.Hotel import Hotel


def parse(player_input):
    player_input = player_input.split()
    command = player_input[0]
    args = player_input[1:]
    for i in range(len(args)):
        try:
            args[i] = int(args[i])
        except ValueError:
            continue
    return command, args


class Console:
    def __init__(self, game):
        self.game = game
        self.current_player_id = 0
        self.dice = Dice()
        self.turn = True
        self.can_throw = True

    def get_player_input(self):
        self.turn = True
        print("Type a command:")
        while self.turn:
            player_input = input()
            [command, args] = parse(player_input)
            try:
                self.__getattribute__(command)(*args)
            except AttributeError:
                print("Wrong command!")
            except ValueError:
                print("Wrong arguments!")

    def get_current_player(self):
        return self.game.get_player(self.current_player_id)

    def next_player(self):
        self.current_player_id += 1
        self.current_player_id %= self.game.player_count
        self.dice = Dice()
        self.turn = False
        self.get_player_input()

    def roll(self):
        if self.can_throw:
            self.dice.throw()
            self.can_throw = self.dice.same()
            if self.dice.repeats < 3:
                self.get_current_player().move(self.dice.value())
            else:
                self.game.get_tile("Jail").put_in_jail(self.get_current_player())

    def buy(self):
        self.game.get_tile(self.get_current_player().position).buy(self.get_current_player())

    def auction(self):
        pass

    def verify_owner(self, target):
        if target is not Hotel:
            print("Tile is not a buildable property!")
            return False
        elif not self.get_current_player().has(target):
            print("You don't own that!")
            return False
        else:
            return True

    def buy_house(self, tile):
        target = self.game.get_tile(tile)
        if self.verify_owner(target):
            target.buy_house()

    def sell_house(self, tile):
        target = self.game.get_tile(tile)
        if self.verify_owner(target):
            target.sell_house()

    def mortgage(self, tile):
        target = self.game.get_tile(tile)
        if self.verify_owner(target):
            target.take_mortgage()

    def repay(self, tile):
        target = self.game.get_tile(tile)
        if self.verify_owner(target):
            target.pay_mortgage()

    def use_card(self):
        if not self.can_throw:
            print("Card must be used before throwing!")
        else:
            self.game.get_tile("Jail").use_card(self.get_current_player())

    def buy_out(self):
        if not self.can_throw:
            print("Buy out must happen before throw!")
        else:
            self.game.get_tile("Jail").buy_out(self.get_current_player())

    def trade(self, *args):
        pass

    def info_player(self, player):
        pass

    def info_tile(self, tile):
        pass
