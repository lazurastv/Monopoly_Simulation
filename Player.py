class Player:
    id = 0

    def __init__(self):
        self.money = 0
        self.position = 0
        self.properties = []
        self.jail_card = False
        self.id = Player.id
        Player.id += 1

    def add_property(self, property_ids):
        for property_id in property_ids:
            self.properties.append(property_id)

    def remove_properties(self, property_ids):
        for property_id in property_ids:
            self.properties.remove(property_id)

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

    def __str__(self):
        return "Player " + str(self.id) + ": $" + str(self.money) + ", " + str(self.properties)