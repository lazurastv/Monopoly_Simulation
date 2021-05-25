class Player:

    def __init__(self, money=1500, position=0, properties=None, card=False):
        self.money = money
        self.position = position
        if properties:
            self.properties = properties
        else:
            self.properties = set()
        self.jail_card = card
        self.start = position

    def __str__(self):
        return "$" + str(self.money) + ", at " + str(self.position)

    def __copy__(self):
        copy = Player(self.money, self.position, self.properties, self.jail_card)
        copy.start = self.start
        return copy

    def add_property(self, tile):
        self.properties.add(tile)

    def remove_property(self, tile):
        self.properties.remove(tile)

    def pay(self, amount, player=None):
        amount //= 1
        self.money -= amount
        try:
            player.earn(amount)
        except AttributeError:
            pass

    def earn(self, amount):
        amount //= 1
        self.money += amount

    def has(self, item):
        try:
            return self.money >= item
        except TypeError:
            return item in self.properties

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

    def get_house_hotel_count(self):
        house_count = 0
        hotel_count = 0
        for tile in self.properties:
            try:
                if tile.has_hotel():
                    hotel_count += 1
                else:
                    house_count += tile.houses
            except AttributeError:
                continue
        return house_count, hotel_count
