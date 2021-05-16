from Player import Player
from Tiles.Property import Property


class Hotel(Property):
    def __init__(self, name, price, mortgage, house_price, rents):
        super().__init__(name, price, mortgage)
        self.house_price = house_price
        self.rents = rents
        self.houses = 0

    def rent(self):
        pass

    def buy_house(self):
        if self.owner and self.owner.has(self.house_price) and self.houses < 5:
            self.houses += 1
            self.owner.pay(self.house_price)

    def sell_house(self):
        if self.owner and self.houses > 0:
            self.houses -= 1
            self.owner.earn(self.house_price)