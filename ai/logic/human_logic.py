from random import random

from ai.logic.auction_logic import AuctionLogic
from ai.logic.logic import Logic
from ai.logic.mortgage_logic import MortgageLogic
from ai.logic.tile_logic import TileLogic
from ai.logic.trading_logic import TradingLogic
from gamecode.control.tile_manager import NotPropertyError
from gamecode.gameplay.trade import TradeError
from gamecode.tiles.jail import Jail
from gamecode.tiles.property import OwnedError, MoneyError


class HumanLogic(Logic):
    def __init__(self, game, index):
        super().__init__(game)
        self.player = game.get_player(index)
        self.mortgage = MortgageLogic(self)
        self.auction_logic = AuctionLogic(self)
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
        if self.can_roll():
            self.normal_move()
        else:
            self.last_move()

    def auction(self):
        self.auction_logic.auction()

    def trade(self):
        self.handle_trade()

    def worth_leaving_jail(self):
        amount = 0
        total = 0
        rent = 0
        board = self.game.board
        for tile in board:
            try:
                if not tile.owned():
                    amount += 1
                elif tile.owned_by(self.player):
                    rent += tile.rent()
                total += 1
            except AttributeError:
                continue
        percent_free = amount / total
        rent /= len(board)
        landings_per_round = len(board) / 7
        jail = board.get("Jail")
        turns_left = jail.turns_left(self.player)
        potential_money = turns_left / landings_per_round * rent * self.game.get_player_count()
        return self.risk_factor > 1 - percent_free or potential_money > Jail.fee

    def normal_move(self):
        self.trader.trade()
        if self.player.in_jail and self.worth_leaving_jail():
            if self.player.jail_card:
                self.run("use_card")
            elif self.player_has_jail_fee():
                self.run("buy_out")
        self.handle_tile()
        self.run("roll")

    def player_has_jail_fee(self):
        return self.player.has(Jail.fee)

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
        if self.risk_factor > random():
            self.handle_tile()
        self.trader.trade()
        if self.player.positive_balance():
            self.tile_logic.manage_tiles()
        else:
            self.mortgage.keep_alive()
        self.handle_tile()
        self.run("next")
