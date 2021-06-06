from gamecode.tiles.tile import Tile


class MortgageError(Exception):
    pass


class Property(Tile):
    def __init__(self, pos, price, mortgage, group=None, mortgaged=False, owner=None):
        super().__init__(pos)
        self.price = price
        self.mortgage = mortgage
        self.group = group
        self.mortgaged = mortgaged
        self.owner = owner

    def __str__(self):
        return super().__str__() + ", " + str(self.group) + ", " + str(self.price)

    def landed_on_event(self, player, dice):
        if self.owner and player != self.owner and not self.mortgaged and not self.owner.in_jail:
            player.pay(self.rent(dice), self.owner)

    def rent(self, dice=None):
        return 0

    def reset(self):
        self.mortgaged = False
        self.owner = None

    def owned(self):
        return self.owner is not None

    def change_owner(self, player):
        if self.owned():
            self.owner.remove_property(self)
        self.owner = player
        player.add_property(self)

    def buy(self, player, price=None):
        if price is None:
            price = self.price
        if self.owned():
            print("Tile already has owner!")
        elif not player.has(price):
            print("Not enough money to purchase!")
        else:
            player.pay(price)
            self.change_owner(player)

    def take_mortgage(self, player):
        if player != self.owner:
            raise MortgageError("You are not the owner!")
        elif self.mortgaged:
            raise MortgageError("Property is already mortgaged!")
        else:
            self.owner.earn(self.mortgage)
            self.mortgaged = True

    def mortgage_pay_cost(self):
        return int(self.mortgage * 1.1)

    def pay_mortgage(self, player):
        amount = self.mortgage_pay_cost()
        if player != self.owner:
            raise MortgageError("You are not the owner!")
        elif not self.mortgaged:
            raise MortgageError("Property isn't mortgaged!")
        elif not self.owner.has(amount):
            raise MortgageError("You don't have the money to pay the mortgage!")
        else:
            self.owner.pay(amount)
            self.mortgaged = False
