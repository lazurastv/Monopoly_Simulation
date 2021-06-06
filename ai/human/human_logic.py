from random import random

from ai.human.auction_logic import AuctionLogic
from ai.human.logic import Logic
from ai.human.mortgage_logic import MortgageLogic
from ai.human.tile_logic import TileLogic
from ai.human.trading_logic import TradingLogic
from gamecode.control.auction import AuctionError
from gamecode.control.tile_manager import NotPropertyError
from gamecode.control.turn_manager import NoThrowsLeftError, TileNotOwnedError
from gamecode.gameplay.trade import TradeError
from gamecode.tiles.property import OwnedError, MoneyError


class HumanLogic(Logic):
    def __init__(self, game, index):
        super().__init__(game)
        self.player = game.get_player(index)
        self.mortgage = MortgageLogic(self)
        self.auction = AuctionLogic(self)
        self.trader = TradingLogic(self)
        self.tile_logic = TileLogic(self)
        self.risk_factor = random()

    def run(self, text):
        self.game.console.run(text)

    def play(self):
        try:
            self.normal_move()
        except AuctionError:
            self.auction.auction()
        except TradeError:
            self.handle_trade()
        except NoThrowsLeftError:
            self.last_move()

    def normal_move(self):
        self.run("me")
        self.trader.trade()
        try:
            self.run("roll")
        except TileNotOwnedError:
            self.handle_tile()
            self.run("roll")
        self.run("dice")

    def handle_tile(self):
        try:
            self.run("buy")
        except MoneyError:
            self.run("auction")
        except (NotPropertyError, OwnedError):
            pass

    def handle_trade(self):
        try:
            self.run("info")
            self.run("accept")
        except TradeError:
            self.run("refuse")

    def last_move(self):
        self.tile_logic.manage_tiles()
        self.trader.trade()
        self.mortgage.keep_alive()
        try:
            self.run("next")
        except TileNotOwnedError:
            self.run("me")
            self.handle_tile()
            self.run("next")
