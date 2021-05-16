from Tiles.Tile import Tile


class Tax(Tile):
    def __init__(self, name, cost):
        super().__init__(name)
        self.cost = cost

    def event(self, player):
        player.pay(self.cost)

    def __str__(self):
        return self.name + " $" + str(self.cost)
