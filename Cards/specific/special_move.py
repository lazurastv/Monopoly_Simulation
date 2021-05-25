from cards.card import Card


class SpecialMove(Card):
    def __init__(self, filename):
        self.filename = filename

    def action(self, game, player):
        target = game.get_nearest(player, self.filename)
        player.move_to(target)
        tile = game.get_tile(target)
        tile.card_rent()
        player.land_on(target)
