from Player import Player


class Players:
    def __init__(self, starting_money, amount):
        self.players = []
        for i in range(amount):
            self.players.append(Player(i, starting_money, None))

    def __iter__(self):
        return iter(self.players)

    def pay(self, amount, player):
        for p in self.players:
            if p != player:
                p.pay(amount, player)

    def get(self, index):
        return self.players[index]

    def count(self):
        return len(self.players)

    def copy(self):
        return self

    def remove(self, player):
        self.players.remove(player)
