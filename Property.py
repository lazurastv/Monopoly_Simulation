class Property:
    id = 0

    def __init__(self, name, price, house_price, rent, mortgage):
        self.name = name
        self.price = price
        self.house_price = house_price
        self.rent = rent
        self.mortgage = mortgage
        self.mortgaged = False
        self.houses = 0
        self.owner = None
        self.id = Property.id
        Property.id += 1

    def event(self, player):
        if self.owner:
            if player != self.owner:
                player.pay(self.rent[self.houses], self.owner)
        else:
            # buy or auction
            pass

    def take_mortgage(self):
        if self.owner and not self.mortgaged:
            self.owner.earn(self.mortgage)
            self.mortgaged = True

    def pay_mortgage(self):
        if self.owner and self.mortgaged:
            self.owner.pay(self.mortgage * 1.1)
            self.mortgaged = False

    def buy_house(self):
        if self.owner and self.owner.can_pay(self.house_price) and self.houses < 5:
            self.owner.pay(self.house_price)
            self.houses += 1

    def sell_house(self):
        if self.owner and self.houses > 0:
            self.owner.earn(self.house_price / 2)
            self.houses -= 1

    def __str__(self):
        return self.name + str(self.id) + str(self.houses) + str(self.owner) + str(self.mortgaged)
