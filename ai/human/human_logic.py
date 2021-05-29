from random import random

from ai.human.auction_logic import AuctionLogic
from ai.human.logic import Logic
from ai.human.trading_logic import TradingLogic
from gamecode.tiles.hotel import Hotel


class HumanLogic(Logic):
    def __init__(self, game, index):
        super().__init__(game)
        self.index = index
        self.player = game.get_player(index)
        self.auction = AuctionLogic(self)
        self.trader = TradingLogic(self)
        self.risk_factor = random()

    def run(self, text):
        self.game.console.run(text)

    def play(self):
        if self.game.console.auction_running():
            self.auction.auction(self.game.console.get_current_tile())
        elif self.game.console.trade_loaded():
            self.run("accept")
        else:
            if self.game.console.turn_mgr.can_roll:
                self.run("roll")
                tile = self.game.console.get_current_tile()
                try:
                    if self.player.has(tile.price):
                        self.run("buy")
                    else:
                        self.run("auction")
                except AttributeError:
                    pass
            else:
                self.keep_alive()
                self.run("next")

    def keep_alive(self):
        targets = self.player.properties.copy()
        for i in range(2):
            for j in range(len(targets)):
                if self.player.positive_balance():
                    return
                tile = targets[j]
                if not tile.mortgaged and ((i == 0 and not tile.group.full_set(self.player))
                                           or (i == 1 and tile.group.highest_house() == 0)):
                    self.run("mortgage " + str(tile.position))
                    targets.remove(tile)
        groups = set()
        for tile in targets:
            groups.add(tile.group)
        for i in range(len(groups)):
            group = groups.pop()
            k = 0
            total = group.total()
            while group.highest_house() != 0:
                if self.player.positive_balance():
                    return
                if group[k] == group.highest_house():
                    self.run("destroy " + str(group[k].id))
                k += 1
                k %= total
            for l in range(total):
                if self.player.positive_balance():
                    return
                self.run("mortgage " + str(group[l]))
