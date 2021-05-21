from tiles.tile import Tile


class Tax(Tile):
    def __init__(self, name, cost):
        super().__init__(name)
        self.cost = cost

    def landed_on_event(self, player, dice):
        player.pay(self.cost)
