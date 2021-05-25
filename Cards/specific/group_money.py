from cards.card import Card


class GroupMoney(Card):
    def __init__(self, amount):
        self.amount = abs(amount)
        self.get = amount > 0

    def action(self, game, player):
        players = game.players
        if self.get:
            players.earn(self.amount, player)
        else:
            players.pay(self.amount, player)

    def __str__(self):
        if self.get:
            return "Get from every player " + str(self.amount)
        else:
            return "Pay every player " + str(self.amount)
