from gamecode.tiles.property import Property


class Train(Property):
    def __init__(self, pos):
        super().__init__(pos, 200, 100)
        self.from_card = False
        self.amount = [0, 25, 50, 100, 200]

    def copy(self, game):
        tile_copy = Train(self.position)
        tile_copy.mortgaged = self.mortgaged
        tile_copy.from_card = self.from_card
        if self.owner:
            player = game.get_player(self.owner.id)
            tile_copy.change_owner(player)
        return tile_copy

    def card_rent(self):
        self.from_card = True

    def rent(self, dice=None):
        if self.owner is None:
            return 0
        val = self.group.count(self.owner)
        if self.from_card:
            self.from_card = False
            return self.amount[val] * 2
        else:
            return self.amount[val]
