from cards.card import Card


class GoBack(Card):
    def action(self, game, player):
        player.move(-3)
