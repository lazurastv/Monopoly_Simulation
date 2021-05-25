from cards.card import Card


class GroupMoney(Card):
    def __init__(self, amount, get):
        self.amount = amount
        self.get = get

    def action(self, game, player):
        players = game.players
        if self.get:
            players.earn(self.amount, player)
        else:
            players.pay(self.amount, player)
