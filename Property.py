from Tile import Tile
from abc import abstractmethod


class Property(Tile):

    def __init__(self, name, index, price, mortgage, group):
        super().__init__(name, index)
        self.price = price
        self.mortgage = mortgage
        self.group = group
        self.mortgaged = False
        self.owner = None

    def event(self, player):
        if self.owner:
            if player != self.owner:
                player.pay(self.rent(), self.owner)
        else:
            # buy or auction
            pass

    @abstractmethod
    def rent(self):
        pass

    def buy(self, player, price=None):
        if not price:
            price = self.price
        if player.has(price):
            player.pay(price)
            self.owner = player
            player.add_property(self)

    def take_mortgage(self):
        if self.owner and not self.mortgaged:
            self.owner.earn(self.mortgage)
            self.mortgaged = True

    def pay_mortgage(self):
        amount = self.mortgage * 1.1
        if self.owner and self.mortgaged and self.owner.has(amount):
            self.owner.pay(amount)
            self.mortgaged = False
