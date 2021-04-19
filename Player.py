class Player:
    id = 0

    def __init__(self):
        self.money = 0
        self.position = 0
        self.id = Player.id
        Player.id += 1

    def pay(self, amount, player=None):
        amount //= 1
        self.money -= amount
        if player:
            player.earn(amount)

    def earn(self, amount):
        amount //= 1
        self.money += amount

    def __str__(self):
        return "Player " + str(self.id) + ": $" + str(self.money)
