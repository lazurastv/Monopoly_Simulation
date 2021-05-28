from gamecode.cards.card import Card


class Money(Card):
    def __init__(self, amount):
        self.amount = abs(amount)
        self.get = amount > 0

    def action(self, game, player):
        if self.get:
            player.earn(self.amount)
        else:
            player.pay(self.amount)

    def __str__(self):
        if self.get:
            return "Get " + str(self.amount)
        else:
            return "Pay " + str(self.amount)
