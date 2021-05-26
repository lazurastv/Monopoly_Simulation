from control.parser import Parser
from gameplay.trade import Trade, TradeException


class Trading:
    def __init__(self, turn_mgr, tile_mgr, game):
        self.trade = None
        self.turn_mgr = turn_mgr
        self.tile_mgr = tile_mgr
        self.players = game.players
        commands = {
            "accept": self.accept,
            "refuse": self.refuse
        }
        self.parser = Parser(commands)

    def run(self, text):
        self.parser.parse_input(text)

    def load(self, player, diff, *tiles):
        player_1 = self.turn_mgr.get_current_player()
        player_2 = self.players.get(player)
        if player_1 == player_2:
            print("You cannot trade with yourself!")
            return
        if len(tiles) == 0:
            print("You cannot give money away for free!")
            return
        tiles = [self.tile_mgr.int_to_tile(x) for x in tiles]
        try:
            self.trade = Trade(player_1, player_2, diff, tiles)
        except TradeException as t:
            print(t)
        except ValueError:
            print("Wrong arguments!")

    def accept(self):
        try:
            self.trade.accept()
        except TradeException:
            print(TradeException)
        except AttributeError:
            print("No trade loaded!")

    def refuse(self):
        if self.trade is None:
            print("No trade loaded!")
        self.trade = None
