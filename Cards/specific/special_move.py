from cards.card import Card


class SpecialMove(Card):
    def __init__(self, tiletype):
        self.tiletype = tiletype

    def action(self, game, player):
        target = game.get_nearest(player, self.tiletype)
        player.move_to(target)
        tile = game.get_tile(target)
        tile.card_rent()
        player.land_on(target)

    def __str__(self):
        return "Special move to " + self.tiletype
