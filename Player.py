class Player:
    id = 0

    def __init__(self, money, position, properties, card=False):
        self.money = money
        self.position = position
        self.properties = properties
        self.jail_card = card
        self.id = Player.id
        Player.id += 1

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

    def has(self, amount):
        return self.money >= amount

    def get_jail_card(self):
        self.jail_card = True

    def has_jail_card(self):
        return self.jail_card

    def use_jail_card(self):
        self.jail_card = False

    def move_to(self, to):
        self.position = to

    def move(self, amount):
        self.position += amount
        self.position %= 40
