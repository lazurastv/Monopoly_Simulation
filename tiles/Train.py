from tiles.property import Property


class Train(Property):
    def __init__(self, name):
        super().__init__(name, 200, 100)

    def rent(self, dice):
        val = self.group.count(self.owner)
        return [0, 25, 50, 100, 200][val]
