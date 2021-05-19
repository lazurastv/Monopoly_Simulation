from Tiles.Property import Property


class Hotel(Property):
    def __init__(self, name, price, mortgage, house_price, rents):
        super().__init__(name, price, mortgage)
        self.house_price = house_price
        self.rents = rents
        self.houses = 0

    def rent(self, dice):
        if self.houses == 0:
            if self.group.full_set(self.owner):
                return self.rents[0] * 2
            else:
                return self.rents[0]
        else:
            return self.rents[self.houses]

    def take_mortgage(self):
        if self.group.has_houses():
            print("You can't take a mortgage on an improved group!")
        else:
            super().take_mortgage()

    def buy_house(self):
        if not self.group.full_set(self.owner):
            print("You don't own the group!")
        elif not self.owner.has(self.house_price):
            print("You can't afford a house! Costs $", self.house_price)
        elif self.houses == 5:
            print("A hotel has already been built!")
        elif self.houses > self.group.lowest_house():
            print("Houses must be built equally!")
        else:
            self.houses += 1
            self.owner.pay(self.house_price)

    def sell_house(self):
        if self.houses == 0:
            print("No houses are built here!")
        elif not self.group.full_set():
            print("Set is not full or is mortgaged!")
        elif self.houses < self.group.highest_house():
            print("Houses must be sold equally!")
        else:
            self.houses -= 1
            self.owner.earn(self.house_price // 2)
