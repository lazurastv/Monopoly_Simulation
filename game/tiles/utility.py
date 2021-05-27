from game.tiles.property import Property


class Utility(Property):
    def __init__(self, pos):
        super().__init__(pos, 150, 75)
        self.from_card = False

    def card_rent(self):
        self.from_card = True

    def rent(self, dice):
        val = self.group.count(self.owner)
        if self.from_card:
            self.from_card = False
            return dice.value() * 10
        elif val == 1:
            return dice.value() * 4
        else:
            return dice.value() * 10
