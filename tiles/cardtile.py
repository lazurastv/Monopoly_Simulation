from tiles.tile import Tile


class CardTile(Tile):
    def __init__(self, pos, deck, game):
        super().__init__(pos)
        self.deck = deck
        self.game = game

    def __str__(self):
        return "Card tile"

    def landed_on_event(self, player, dice):
        card = self.deck.draw()
        print(card)
        card.action(self.game, player)
