from Tiles.Tile import Tile


class Tax(Tile):
    def __init__(self, name, index, cost):
        super().__init__(name, index)
        self.cost = cost

    def event(self, player):
        player.pay(self.cost)
