from tiles.property import Property


class Train(Property):
    def __init__(self, name):
        super().__init__(name, 200, 100)
        self.from_card = False

    def card_rent(self):
        self.from_card = True

    def rent(self, dice):
        val = self.group.count(self.owner)
        amount = [0, 25, 50, 100, 200][val]
        if self.from_card:
            self.from_card = False
            return amount * 2
        else:
            return amount
