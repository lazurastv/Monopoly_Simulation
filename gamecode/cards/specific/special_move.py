from gamecode.cards.card import Card
from gamecode.gameplay.dice import Dice


class SpecialMove(Card):
    def __init__(self, tiletype):
        self.tiletype = tiletype

    def action(self, game, player):
        target = game.get_nearest(player, self.tiletype)
        player.move_to(target)
        tile = game.get_tile(target)
        tile.card_rent()
        dice = Dice()
        dice.roll()
        player.land_on(tile, dice)

    def __str__(self):
        return "Special move to " + self.tiletype
