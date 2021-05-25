from cards.card import Card


class GoBack(Card):
    def action(self, game, player):
        player.move(-3)

    def __str__(self):
        return "Go back three spaces"
