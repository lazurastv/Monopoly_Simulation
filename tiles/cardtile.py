from tiles.tile import Tile


class CardTile(Tile):
    def __init__(self, pos, deck, game):
        super().__init__(pos)
        self.deck = deck
        self.game = game

    def landed_on_event(self, player, dice):
        self.deck.draw().action(self.game, player)
