import json
from pathlib import Path

import control.tile_managing as tile_managing
from control.auction import Auction, parse
from control.trading import Trading
from gameplay.dice import Dice


class Console:
    def __init__(self, game):
        self.game = game
        self.dice = Dice()
        self.trading = Trading()
        self.can_throw = True
        self.current_player_id = 0
        with open(Path(__file__).parent / "../data/valid_commands.json") as commands:
            self.valid_commands = json.load(commands)["commands"]

    def get_player_input(self):
        while True:
            player_input = input()
            [command, args] = parse(player_input)
            try:
                self.run(command, args)
            except TypeError:
                print("Wrong command!")
            except ValueError:
                print("Wrong arguments!")

    def run(self, command, args):
        if command not in self.valid_commands:
            raise TypeError
        else:
            getattr(Console, command)(self, *args)

    def get_current_player(self):
        return self.game.get_player(self.current_player_id)

    def get_current_tile(self):
        return self.game.get_tile(self.get_current_player().position)

    def get_player(self, player):
        return self.game.get_player(player)

    def get_tile(self, tile):
        return self.game.get_tile(tile)

    def next_player(self):
        self.current_player_id += 1
        self.current_player_id %= self.game.player_count()
        self.dice = Dice()

    def roll(self):
        if not self.can_throw:
            print("No more throws left this turn!")
        else:
            self.dice.throw()
            self.can_throw = self.dice.same()
            current_player = self.get_current_player()
            if self.dice.repeats < 3:
                current_player.start_from(self.get_current_tile(), self.dice)
                current_player.land_on(self.get_current_tile(), self.dice)
            else:
                self.get_tile("Jail").put_in_jail(current_player)

    def buy(self):
        tile_managing.buy(self.get_current_tile(), self.get_current_player())

    def buy_house(self, tile):
        tile_managing.buy_house(self.get_tile(tile), self.get_current_player())

    def sell_house(self, tile):
        tile_managing.sell_house(self.get_tile(tile), self.get_current_player())

    def mortgage(self, tile):
        tile_managing.mortgage(self.get_tile(tile), self.get_current_player())

    def repay(self, tile):
        tile_managing.repay(self.get_tile(tile), self.get_current_player())

    def auction(self):
        auc = Auction(self.get_current_tile(), self.game.players)
        auc.start()

    def use_card(self):
        if not self.can_throw:
            print("Card must be used before throwing!")
        else:
            self.get_tile("Jail").use_card(self.get_current_player())

    def buy_out(self):
        if not self.can_throw:
            print("Buy out must happen before throw!")
        else:
            self.get_tile("Jail").buy_out(self.get_current_player())

    def trade(self, player_id, give, *tiles):
        self.trading.load(self.get_current_player(), self.get_player(player_id), give, tiles)

    def accept(self):
        self.trading.accept(self.get_current_player())

    def refuse(self):
        self.trading.refuse(self.get_current_player())

    def info_me(self):
        print(self.get_current_player())

    def info_player(self, player):
        print(self.get_player(player))

    def info_tile(self, tile):
        print(self.get_tile(tile))

    def info_dice(self):
        print(self.dice)
