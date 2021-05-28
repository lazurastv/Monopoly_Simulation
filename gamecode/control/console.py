from gamecode.control.auction import Auction
from gamecode.control.information import Information
from gamecode.control.parser import Parser
from gamecode.control.tile_manager import TileManager
from gamecode.control.trading import Trading
from gamecode.control.turn_manager import TurnManager


class Console:
    def __init__(self, game):
        self.info = Information(game)
        self.turn_mgr = TurnManager(game)
        self.tile_mgr = TileManager(game)
        self.auction = Auction(game)
        self.trading = Trading(game)
        commands = {
            "roll": self.turn_mgr.roll,
            "next": self.turn_mgr.next,
            "auction": self.auction.start,
            "buy": self.tile_mgr.buy,
            "build": self.tile_mgr.buy_house,
            "destroy": self.tile_mgr.sell_house,
            "mortgage": self.tile_mgr.mortgage,
            "repay": self.tile_mgr.repay,
            "use_card": self.turn_mgr.use_card,
            "buy_out": self.turn_mgr.buy_out,
            "trade": self.trading.load,
            "accept": self.trading.accept,
            "refuse": self.trading.refuse,
            "me": self.turn_mgr.info_current_player,
            "player": self.info.info_player,
            "tile": self.info.info_tile,
            "dice": self.turn_mgr.info_dice
        }
        self.parser = Parser(commands)

    def auction_running(self):
        return self.auction.running

    def trade_loaded(self):
        return self.trading.trade is not None

    def get_current_player(self):
        return self.turn_mgr.get_current_player()

    def get_current_tile(self):
        return self.turn_mgr.get_current_tile()

    def get_tile(self, tile):
        return self.info.get_tile(tile)

    def current_tile_owned(self):
        return self.turn_mgr.current_tile_owned()

    def run(self, text):
        if self.trade_loaded():
            self.trading.run(text)
        elif self.auction_running():
            self.auction.run(text)
        else:
            self.parser.parse_input(text)
