from Player import Player


class Players:
    def __init__(self, starting_money, amount):
        self.players = []
        for i in range(amount):
            self.players.append(Player(i, starting_money, None))

    def pay(self, amount, player):
        for p in self.players:
            if p != player:
                p.pay(amount, player)