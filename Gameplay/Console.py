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
        self.get_player_input()

    def get_current_player(self):
        return self.game.get_player(self.current_player_id)

    def get_tile(self, tile):
        return self.game.get_tile(tile)

    def next_player(self):
        self.current_player_id += 1
        self.current_player_id %= self.game.player_count()
        self.dice = Dice()
        self.turn = False

    def roll(self):
        if not self.can_throw:
            print("No more throws left this turn!")
        else:
            self.dice.throw()
            self.can_throw = self.dice.same()
            current_player = self.get_current_player()
            if self.dice.repeats < 3:
                current_player.start_from(self.get_tile(current_player.position), self.dice)
                current_player.land_on(self.get_tile(current_player.position), self.dice)
            else:
                self.get_tile("Jail").put_in_jail(current_player)

    def buy(self):
        current_player = self.get_current_player()
        try:
            self.get_tile(current_player.position).buy(current_player)
        except AttributeError:
            print("Tile is not a property!")

    def auction_for(self, amount):
        current_player = self.get_current_player()
        self.get_tile(current_player.position).buy(current_player, amount)

    def auction(self):
        pass

    def buy_house(self, tile):
        try:
            self.get_tile(tile).buy_house(self.get_current_player())
        except AttributeError:
            print("Tile is not an improvable tile!")

    def sell_house(self, tile):
        try:
            self.get_tile(tile).sell_house(self.get_current_player())
        except AttributeError:
            print("Tile is not an improvable tile!")

    def mortgage(self, tile):
        try:
            self.get_tile(tile).take_mortgage(self.get_current_player())
        except AttributeError:
            print("Tile is not a property!")

    def repay(self, tile):
        try:
            self.get_tile(tile).pay_mortgage(self.get_current_player())
        except AttributeError:
            print("Tile is not a property!")

    def use_card(self):
        if not self.can_throw:
            print("Card must be used before throwing!")
        else:
            self.get_tile("Jail").use_card(self.get_current_player())

    def buy_out(self):
        if not self.can_throw:
            print("Buy out must happen before throw!")
        else:
            self.game.get_tile("Jail").buy_out(self.get_current_player())

    def trade(self, *args):
        pass

    def refuse(self):
        pass

    def accept(self):
        pass

    def info_player(self, player):
        print(self.game.get_player(player))

    def info_tile(self, tile):
        print(self.get_tile(tile))

    def info_dice(self):
        print(self.dice)
