from cards.card import Card


class GetOut(Card):
    def action(self, game, player):
        player.get_jail_card()
