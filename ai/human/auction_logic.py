from gamecode.tiles.hotel import Hotel
from gamecode.tiles.utility import Utility


class AuctionLogic:
    def __init__(self, logic):
        self.logic = logic
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
        max_owned = max([group.count(x) for x in self.logic.game.players])
        mine = group.count(self.logic.player)
        total = group.total()
        ratio = (mine, total)
        worst = (max_owned, total)
        if worst == (2, 3) or worst == (1, 2):
            return self.logic.player.money
        elif mine == 0:
            return 4 * self.target.rents[0]
        elif ratio == (1, 3):
            return 6 * self.target.rents[0]
        elif self.target.rents[5] < 500:
            return 2 * self.target.rents[5]
        else:
            return self.logic.player.money

    def max_auction_value_for_utility(self):
        group = self.target.group
        mine = group.count(self.logic.player)
        if mine == 0:
            return self.target.price / 2
        else:
            return self.target.price * 2

    def max_auction_value_for_railroad(self):
        group = self.target.group
        max_owned = max([group.count(x) for x in self.logic.game.players])
        mine = group.count(self.logic.player)
        if max_owned == 2:
            return self.target.price * 1.5
        elif max_owned == 3:
            return self.target.price * 3
        elif mine == 0:
            return self.target.price / 2
        elif mine == 1:
            return self.target.price
        elif mine == 2:
            return self.target.price * 2
        elif mine == 3:
            return self.target.price * 4

    def auction(self, tile):
        if tile == self.target:
            val = self.logic.game.console.auction.value
            if val < self.max_value and self.logic.player.has(val):
                self.logic.run("bet " + str(val))
            else:
                self.logic.run("end")
        else:
            self.target = tile
            self.max_value = self.max_auction_value()
