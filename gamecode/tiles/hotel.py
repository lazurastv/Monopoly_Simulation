from gamecode.tiles.property import Property, MortgageError


class HouseError(Exception):
    pass


class Hotel(Property):
    def __init__(self, pos, price, mortgage, house_price, rents):
        super().__init__(pos, price, mortgage)
        self.house_price = house_price
        self.rents = rents
        self.houses = 0

    def __str__(self):
        addon = ""
        if self.owner:
            addon = ", rent = " + str(self.rent(None))
        return super().__str__() + addon

    def rent(self, dice=None):
        if self.owner is None:
            return 0
        elif self.houses == 0 and self.group.owned_by(self.owner):
            return self.rents[0] * 2
        else:
            return self.rents[self.houses]

    def rent_change(self):
        self.houses += 1
        dfx = 0
        try:
            dfx = self.rent()
        except IndexError:
            pass
        self.houses -= 1
        return dfx

    def reset(self):
        super().reset()
        self.houses = 0

    def has_hotel(self):
        return self.houses == 5

    def group_owned(self):
        return self.group.owned_by(self.owner)

    def take_mortgage(self, player):
        if self.group.has_houses():
            raise MortgageError("You can't take a mortgage on an improved group!")
        else:
            super().take_mortgage(player)

    def buy_house(self, player):
        if player != self.owner:
            raise HouseError("You are not the owner!")
        elif not self.group_owned():
            raise HouseError("You don't own the group!")
        elif not self.owner.has(self.house_price):
            raise HouseError("You can't afford a house! Costs $", self.house_price)
        elif self.houses == 5:
            raise HouseError("A hotel has already been built!")
        elif self.houses > self.group.lowest_house():
            raise HouseError("Houses must be built equally!")
        else:
            self.houses += 1
            self.owner.pay(self.house_price)

    def sell_house(self, player):
        if player != self.owner:
            raise HouseError("You are not the owner!")
        elif self.houses == 0:
            raise HouseError("No houses are built here!")
        elif self.houses < self.group.highest_house():
            raise HouseError("Houses must be sold equally!")
        else:
            self.houses -= 1
            self.owner.earn(self.house_price // 2)
