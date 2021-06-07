from random import random

from ai.human.auction_logic import AuctionLogic
from ai.human.logic import Logic
from ai.human.mortgage_logic import MortgageLogic
from ai.human.tile_logic import TileLogic
from ai.human.trading_logic import TradingLogic
from gamecode.control.tile_manager import NotPropertyError
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

    def copy(self, game):
        logic_copy = HumanLogic(game, self.player.id)
        logic_copy.risk_factor = self.risk_factor
        return logic_copy

    def run(self, text):
        self.game.console.run(text)

    def auction_running(self):
        return self.game.console.auction_running()

    def trade_loaded(self):
        return self.game.console.trade_loaded()

    def can_roll(self):
        return self.game.console.turn_mgr.can_roll

    def current_tile_owned(self):
        return self.game.console.current_tile_owned()

    def play(self):
        if self.auction_running():
            self.auction.auction()
        elif self.trade_loaded():
            self.handle_trade()
        elif self.can_roll():
            self.normal_move()
        else:
            self.last_move()

    def normal_move(self):
        self.trader.trade()
        self.run("roll")
        if not self.current_tile_owned():
            self.handle_tile()

    def handle_tile(self):
        try:
            self.run("buy")
        except MoneyError:
            self.run("auction")
        except (NotPropertyError, OwnedError):
            pass

    def handle_trade(self):
        try:
            self.run("accept")
        except TradeError:
            self.run("refuse")

    def last_move(self):
        self.tile_logic.manage_tiles()
        self.trader.trade()
        self.mortgage.keep_alive()
        try:
            if not self.current_tile_owned():
                self.handle_tile()
        except AttributeError:
            pass
        self.run("next")
