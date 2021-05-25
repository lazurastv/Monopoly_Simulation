from cards.card import Card


class Money(Card):
    def __init__(self, amount, get):
        self.amount = amount
        self.get = get

    def action(self, game, player):
        if self.get:
            player.earn(self.amount)
        else:
            player.pay(self.amount)
