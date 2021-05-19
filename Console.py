from Dice import Dice


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
        self.dice.throw()

    def buy(self):
        self.game.buy(self.get_current_player(), self.get_current_player().position)

    def auction(self):
        pass

    def buy_house(self, tile):
        pass

    def sell_house(self, tile):
        pass

    def mortgage(self, tile):
        pass

    def repay(self, tile):
        pass

    def use_card(self):
        pass

    def buy_out(self):
        pass

    def trade(self, *args):
        pass

    def info_player(self, player):
        pass

    def info_tile(self, tile):
        pass
