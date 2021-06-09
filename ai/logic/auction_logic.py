from ai.logic.sub_logic import SubLogic
from gamecode.tiles.hotel import Hotel
from gamecode.tiles.utility import Utility


class AuctionLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)
        self.max_value = None
        self.target = None

    def max_auction_value(self):
        if isinstance(self.target, Hotel):
            return self.max_auction_value_for_hotel()
        elif isinstance(self.target, Utility):
            return self.max_auction_value_for_utility()
        else:
            return self.max_auction_value_for_railroad()

    def max_auction_value_for_hotel(self):
        group = self.target.group
        max_owned = group.max_ownership(self.logic.game.players)
        mine = group.count_owned(self.logic.player)
        total = len(group)
        ratio = (mine, total)
        worst = (max_owned, total)
        if ratio == (2, 3) or ratio == (1, 2):
            return self.logic.player.money
        elif worst == (2, 3) or worst == (1, 2):
            return self.logic.player.money
        elif ratio == (1, 3):
            return self.target.price * 2
        else:
            return self.target.price * 1.5

    def max_auction_value_for_utility(self):
        group = self.target.group
        mine = group.count_owned(self.logic.player)
        if mine == 0:
            return self.target.price / 2
        else:
            return self.target.price * 2

    def max_auction_value_for_railroad(self):
        group = self.target.group
        max_owned = group.max_ownership(self.logic.game.players)
        mine = group.count_owned(self.logic.player)
        if mine == 3:
            return self.target.price * 4
        elif max_owned == 3:
            return self.target.price * 3
        elif mine == 2:
            return self.target.price * 2
        elif max_owned == 2:
            return self.target.price * 1.5
        elif mine == 1:
            return self.target.price
        elif mine == 0:
            return self.target.price / 2

    def auction(self):
        if self.get_current_tile() is self.target:
            val = self.logic.game.console.auction.value + 1
            if val < self.max_value and self.logic.player.has(val):
                self.run("bet " + str(val))
            else:
                self.run("end")
        else:
            self.target = self.get_current_tile()
            self.max_value = self.max_auction_value() * (1 + 2 * self.logic.risk_factor) / 2
