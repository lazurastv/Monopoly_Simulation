from gamecode.control.parser import Parser, ParserError
from gamecode.gameplay.trade import Trade, TradeError


class Trading:
    def __init__(self, game):
        self.trade = None
        self.game = game
        commands = {
            "accept": self.accept,
            "refuse": self.refuse,
            "info": self.info
        }
        self.parser = Parser(commands)

    def run(self, text):
        try:
            self.parser.parse_input(text)
        except ParserError:
            raise TradeError

    def trade_loaded(self):
        return self.trade is not None

    def int_to_tile(self, val):
        return self.game.console.tile_mgr.int_to_tile(val)

    def load(self, player, diff, *tiles):
        player_1 = self.game.console.get_current_player()
        player_2 = self.game.players.get_by_id(player)
        if player_1 == player_2:
            raise TradeError("You cannot trade with yourself!")
        if len(tiles) == 0:
            raise TradeError("You cannot give money away for free!")
        tiles = [self.int_to_tile(x) for x in tiles]
        try:
            self.trade = Trade(player_1, player_2, diff, tiles)
        except ValueError:
            print("Wrong arguments!")
        while self.trade_loaded():
            player_2.play()

    def accept(self):
        try:
            self.trade.accept()
            self.trade = None
        except AttributeError:
            raise TradeError("No trade loaded!")

    def refuse(self):
        if self.trade is None:
            raise TradeError("No trade loaded!")
        self.trade = None

    def info(self):
        print(self.trade)
