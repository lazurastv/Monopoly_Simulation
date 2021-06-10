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

    def copy(self, game):
        hotel_copy = Hotel(self.position, self.price, self.mortgage, self.house_price, self.rents)
        hotel_copy.mortgaged = self.mortgaged
        hotel_copy.houses = self.houses
        if self.owner:
            player = game.get_player_by_id(self.owner.id)
            hotel_copy.change_owner(player)
        return hotel_copy

    def rent(self, dice=None):
        if self.owner is None:
            return 0
        elif self.houses == 0 and self.group.owned_and_not_mortgaged(self.owner):
            return self.rents[0] * 2
        else:
            return self.rents[self.houses]

    def derivative(self, sell=False):
        if sell:
            money = self.sell_house_value()
            dx = -1
        else:
            money = self.house_price + self.group.pay_all_mortgage_cost()
            dx = 1
        dfx = self.rent()
        self.houses += dx
        try:
            dfx = self.rent() - dfx
        except IndexError:
            dfx = 0
        self.houses -= dx
        return dfx / money

    def reset(self):
        super().reset()
        self.houses = 0

    def has_hotel(self):
        return self.houses == 5

    def take_mortgage(self, player):
        if self.group.has_houses():
            raise MortgageError("You can't take a mortgage on an improved group!")
        else:
            super().take_mortgage(player)

    def can_buy_house(self, player):
        return player == self.owner and self.group.owned_and_not_mortgaged(player) \
               and self.owner.has(self.house_price) and not self.has_hotel() \
               and self.even()

    def buy_house(self, player):
        if self.can_buy_house(player):
            self.houses += 1
            self.owner.pay(self.house_price)
        else:
            raise HouseError("You can't buy a house!")

    def can_sell_house(self, player):
        return player == self.owner and self.houses > 0 and self.even(True)

    def even(self, sell=False):
        if sell:
            return self.houses == self.group.highest_house()
        else:
            return self.houses == self.group.lowest_house()

    def sell_house_value(self):
        return self.house_price // 2

    def sell_house(self, player):
        if self.can_sell_house(player):
            self.houses -= 1
            self.owner.earn(self.sell_house_value())
        else:
            raise HouseError("You can't sell a house!")
