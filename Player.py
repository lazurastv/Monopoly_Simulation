class Player:
    id = 0

    def __init__(self, money, position):
        self.money = money
        self.id = Player.id
        self.position = position
        Player.id += 1

    def __str__(self):
        return "Player " + str(self.id) + ": $" + str(self.money)

    def pay(self, amount, player=None):
        self.money -= amount
        if player:
            player.earn(amount)

    def earn(self, amount):
        self.money += amount
