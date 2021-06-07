from gamecode.tiles.tile import Tile


class Tax(Tile):
    def __init__(self, pos, cost):
        super().__init__(pos)
        self.cost = cost

    def __str__(self):
        return super().__str__() + ", $" + str(self.cost)

    def copy(self, game):
        return Tax(self.position, self.cost)

    def landed_on_event(self, player, dice):
        player.pay(self.cost)
