from Tiles.Property import Property


class Player:

    def __init__(self, id_num, money, game, position=0, properties=None, card=False):
        self.money = money
        self.position = position
        self.properties = []
        if properties:
            self.properties = properties
        self.game = game
        self.jail_card = card
        self.id = id_num

    def __str__(self):
        return str(self.id) + ": $" + str(self.money) + ", at " + str(self.position)

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

    def has(self, item):
        if item is int or item is float:
            return self.money >= item
        elif issubclass(Property, item.__class__):
            return item in self.properties
        else:
            return False

    def get_jail_card(self):
        self.jail_card = True

    def has_jail_card(self):
        return self.jail_card

    def use_jail_card(self):
        self.jail_card = False

    def move_to(self, to):
        start = self.position
        self.position = to
        self.crossed_start(start)

    def move(self, amount):
        start = self.position
        self.position += amount
        self.position %= 40
        self.crossed_start(start)
        self.tile_on().landed_on_event(amount)

    def tile_on(self):
        return self.game.board.get_index(self.position)

    def crossed_start(self, start):
        if start > self.position:
            self.earn(200)
