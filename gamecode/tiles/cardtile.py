from copy import deepcopy

from gamecode.tiles.tile import Tile


class CardTile(Tile):
    def __init__(self, pos, deck, game):
        super().__init__(pos)
        self.deck = deck
        self.game = game

    def __str__(self):
        return "Card tile"

    def copy(self, game):
        deck_copy = deepcopy(self.deck)
        return CardTile(self.position, deck_copy, game)

    def landed_on_event(self, player, dice):
        card = self.deck.draw()
        card.action(self.game, player)
