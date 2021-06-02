from random import random

from ai.human.auction_logic import AuctionLogic
from ai.human.logic import Logic
from ai.human.mortgage_logic import MortgageLogic
from ai.human.tile_logic import TileLogic
from ai.human.trading_logic import TradingLogic


class HumanLogic(Logic):
    def __init__(self, game, index):
        super().__init__(game)
        self.index = index
        self.player = game.get_player(index)
        self.mortgage = MortgageLogic(self)
        self.auction = AuctionLogic(self)
        self.trader = TradingLogic(self)
        self.tile_logic = TileLogic(self)
        self.risk_factor = random()

    def run(self, text):
        self.game.console.run(text)

    def play(self):
        if self.game.console.auction_running():
            self.auction.auction(self.game.console.get_current_tile())
        elif self.game.console.trade_loaded():
            self.run("info")
            self.run("accept")
        else:
            if self.game.console.turn_mgr.can_roll:
                self.normal_move()
            else:
                self.last_move()

    def normal_move(self):
        self.run("me")
        self.run("roll")
        self.run("dice")
        self.run("buy")
        self.run("auction")

    def last_move(self):
        self.run("me")
        self.tile_logic
        self.mortgage.keep_alive()
        self.run("next")