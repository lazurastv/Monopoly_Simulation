from gamecode.cards.card import Card


class GetOut(Card):
    def action(self, game, player):
        player.get_jail_card()

    def __str__(self):
        return "Get out of jail free card"
