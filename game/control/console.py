from game.control.auction import Auction
from game.control.information import Information
from game.control.parser import Parser
from game.control.tile_manager import TileManager
from game.control.trading import Trading
from game.control.turn_manager import TurnManager


class Console:
    def __init__(self, game):
        self.info = Information(game)
        self.turn_mgr = TurnManager(self.info, game)
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

    def run(self, text):
        if self.auction.running:
            return self.auction.run(text)
        elif self.trading.trade:
            return self.trading.run(text)
        else:
            return self.parser.parse_input(text)
