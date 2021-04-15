class Property:
    id = 0

    def __init__(self, name, price, house_price, rent, mortgage):
        self.name = name
        self.price = price
        self.house_price = house_price
        self.rent = rent
        self.mortgage = mortgage
        self.houses = 0
        self.owner = None
        self.id = Property.id
        Property.id += 1

    def event(self, player):
        if self.owner:
            player.pay(self.owner)

    def mortgage(self):
        pass
