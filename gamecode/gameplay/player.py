class Player:
    def __init__(self, index, money=1500, position=0, properties=None, card=False):
        self.id = index
        self.logic = None
        self.money = money
        self.position = position
        if properties:
            self.properties = properties
        else:
            self.properties = set()
        self.jail_card = card
        self.start = position
        self.in_jail = False

    def __str__(self):
        text = str(self.id) + ", " + str(self.money) + ", at " + str(self.position) + ", owns: "
        for tile in self.properties:
            text += str(tile.position) + ", "
        return text

    def __deepcopy__(self, memodict={}):
        player_copy = Player(self.id, self.money, self.position, card=self.jail_card)
        player_copy.start = self.start
        player_copy.in_jail = self.in_jail
        return player_copy

    def inject_logic(self, logic):
        self.logic = logic

    def add_property(self, tile):
        self.properties.add(tile)

    def remove_property(self, tile):
        self.properties.remove(tile)

    def pay(self, amount, player=None):
        amount = int(amount)
        self.money -= amount
        try:
            player.earn(amount)
        except AttributeError:
            pass

    def earn(self, amount):
        amount = int(amount)
        self.money += amount

    def has(self, item):
        try:
            return self.money >= item
        except TypeError:
            return item in self.properties

    def positive_balance(self):
        return self.money >= 0

    def get_jail_card(self):
        self.jail_card = True

    def has_jail_card(self):
        return self.jail_card

    def use_jail_card(self):
        self.jail_card = False

    def move_to(self, index):
        self.start = self.position
        self.position = index
        self.crossed_start_bonus()

    def move(self, amount):
        self.start = self.position
        self.position += amount
        self.position %= 40
        self.crossed_start_bonus()

    def start_from(self, tile, dice):
        tile.starting_from_event(self, dice)

    def land_on(self, tile, dice):
        tile.landed_on_event(self, dice)

    def crossed_start_bonus(self):
        if self.start > self.position and not self.in_jail:
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

    def kill(self):
        for tile in self.properties:
            tile.reset()

    def play(self):
        self.logic.play()

    def auction(self):
        self.logic.auction()

    def trade(self):
        self.logic.trade()
