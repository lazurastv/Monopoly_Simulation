from Tiles.Property import Property


class Player:

    def __init__(self, money=1500, position=0, properties=None, card=False):
        self.money = money
        self.position = position
        if properties:
            self.properties = properties
        else:
            self.properties = []
        self.jail_card = card
        self.start = position

    def __str__(self):
        return "$" + str(self.money) + ", at " + str(self.position)

    def __eq__(self, other):
        return other is Player and str(self) == str(other)

    def add_property(self, tile):
        self.properties.append(tile)

    def remove_property(self, tile):
        self.properties.remove(tile)

    def pay(self, amount, player=None):
        amount //= 1
        self.money -= amount
        if player:
            player.earn(amount)

    def earn(self, amount):
        amount //= 1
        self.money += amount

    def has_money(self, amount):
        return self.money >= amount

    def has_property(self, tile):
        return tile in self.properties

    def get_jail_card(self):
        self.jail_card = True

    def has_jail_card(self):
        return self.jail_card

    def use_jail_card(self):
        self.jail_card = False

    def move_to(self, index):
        self.start = self.position
        self.position = index

    def move(self, amount):
        self.start = self.position
        self.position += amount
        self.position %= 40

    def start_from(self, tile, dice):
        tile.starting_from_event(self, dice)

    def land_on(self, tile, dice):
        tile.landed_on_event(self, dice)

    def crossed_start_bonus(self):
        if self.start > self.position:
            self.earn(200)
