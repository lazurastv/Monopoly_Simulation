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
        if self.owner and player != self.owner:
            player.pay(self.rent(dice), self.owner)

    def rent(self, dice):
        return 0

    def buy(self, player, price=None):
        if not isinstance(price, int):
            price = self.price
        if not player.has(price):
            print("Not enough money to purchase!")
        else:
            player.pay(price)
            self.owner = player
            player.add_property(self)

    def take_mortgage(self):
        if self.mortgaged:
            print("Property is already mortgaged!")
        else:
            self.owner.earn(self.mortgage)
            self.mortgaged = True

    def pay_mortgage(self):
        amount = self.mortgage * 1.1
        if not self.mortgaged:
            print("Property isn't mortgaged!")
        elif not self.owner.has(amount):
            print("You don't have the money to pay the mortgage!")
        else:
            self.owner.pay(amount)
            self.mortgaged = False
