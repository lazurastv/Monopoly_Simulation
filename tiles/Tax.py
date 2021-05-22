from tiles.tile import Tile


class Tax(Tile):
    def __init__(self, name, cost):
        super().__init__(name)
        self.cost = cost

    def __str__(self):
        return super().__str__() + ", $" + str(self.cost)

    def landed_on_event(self, player, dice=None):
        player.pay(self.cost)
