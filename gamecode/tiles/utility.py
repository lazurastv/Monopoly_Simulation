from gamecode.tiles.property import Property


class Utility(Property):
    def __init__(self, pos):
        super().__init__(pos, 150, 75)
        self.from_card = False

    def copy(self, game):
        tile_copy = Utility(self.position)
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
        val = self.group.count_owned_and_not_mortgaged(self.owner)
        dice_value = 7
        if dice is not None:
            dice_value = dice.value()
        if self.from_card:
            self.from_card = False
            return dice_value * 10
        elif val == 1:
            return dice_value * 4
        else:
            return dice_value * 10
