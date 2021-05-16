from Tiles.Tile import Tile


class Tax(Tile):
    def __init__(self, name, cost, board):
        super().__init__(name, board)
        self.cost = cost

    def landed_on_event(self, player, dice):
        player.pay(self.cost)

    def __str__(self):
        return self.name + " $" + str(self.cost)
