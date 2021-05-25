from tiles.property import Property


class Train(Property):
    def __init__(self, pos):
        super().__init__(pos, 200, 100)
        self.from_card = False
        self.amount = [0, 25, 50, 100, 200]

    def card_rent(self):
        self.from_card = True

    def rent(self, dice):
        val = self.group.count(self.owner)
        if self.from_card:
            self.from_card = False
            return self.amount[val] * 2
        else:
            return self.amount[val]
