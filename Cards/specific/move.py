from cards.card import Card


class Move(Card):
    def __init__(self, tile):
        self.tile = tile

    def action(self, game, player):
        true_tile = game.get_tile(self.tile)
        tile_index = game.board.index_of(self.tile)
        player.move_to(tile_index)
        player.land_on(true_tile, None)

    def __str__(self):
        return "Go to " + str(self.tile)
