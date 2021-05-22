from tiles.tile import Tile


class CardTile(Tile):
    def __init__(self, name, deck):
        super().__init__(name)
        self.deck = deck

    def landed_on_event(self, player, dice):
        self.deck.draw()
