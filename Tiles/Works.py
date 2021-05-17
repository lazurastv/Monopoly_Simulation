from Tiles.Property import Property


class Works(Property):
    def __init__(self, name):
        super().__init__(name, 150, 75)

    def rent(self, dice):
        val = self.group.count(self.owner)
        if val == 1:
            return dice.value * 4
        else:
            return dice.value * 10
