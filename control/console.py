from control.auction import Auction
from control.information import Information
from control.parser import Parser
from control.tile_manager import TileManager
from control.trading import Trading
from control.turn_manager import TurnManager


class Console:
    def __init__(self, game):
        self.info = Information(game)
        self.turn_mgr = TurnManager(self.info)
        self.tile_mgr = TileManager(self.turn_mgr, self.info)
        self.auction = Auction(self.turn_mgr, game.players)
        self.trading = Trading(self.turn_mgr, self.tile_mgr, game)
        commands = {
            "roll": self.turn_mgr.roll,
            "next": self.turn_mgr.next,
            "auction": self.auction.start,
            "buy": self.tile_mgr.buy,
            "build": self.tile_mgr.buy_house,
            "destroy": self.tile_mgr.sell_house,
            "mortgage": self.tile_mgr.mortgage,
            "repay": self.tile_mgr.repay,
            "use card": self.turn_mgr.use_card,
            "buy out": self.turn_mgr.buy_out,
            "trade": self.trading.load,
            "accept": self.trading.accept,
            "refuse": self.trading.refuse,
            "me": self.turn_mgr.info_current_player,
            "player": self.info.info_player,
            "tile": self.info.info_tile,
            "dice": self.turn_mgr.info_dice
        }
        self.parser = Parser(commands)

    def run(self, text):
        if self.auction.running:
            self.auction.run(text)
        elif self.trading.trade:
            self.trading.run(text)
        else:
            self.parser.parse_input(text)