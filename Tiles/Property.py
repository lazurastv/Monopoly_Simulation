from Tile import Tile


class Property(Tile):

    def __init__(self, name, price, mortgage, group=None, mortgaged=False, owner=None):
        super().__init__(name)
        self.price = price
        self.mortgage = mortgage
        self.group = group
        self.mortgaged = mortgaged
        self.owner = owner

    def __str__(self):
        return super().__str__() + ": $" + str(self.price) + " => $" + str(self.owner) + " " + str(self.group)

    def landed_on_event(self, player, dice):
        if self.owner:
            if player != self.owner:
                player.pay(self.rent(dice), self.owner)
            return True
        else:
            return False

    def rent(self, dice):
        return 0

    def set_group(self, group):
        self.group = group

    def buy(self, player, price=None):
        if not isinstance(price, int):
            price = self.price
        if player.has(price):
            player.pay(price)
            self.owner = player
            player.add_property(self)

    def owns(self, player):
        return self.owner == player

    def take_mortgage(self):
        if self.owner and not self.mortgaged:
            self.owner.earn(self.mortgage)
            self.mortgaged = True

    def pay_mortgage(self):
        amount = self.mortgage * 1.1
        if self.owner and self.mortgaged and self.owner.has(amount):
            self.owner.pay(amount)
            self.mortgaged = False
