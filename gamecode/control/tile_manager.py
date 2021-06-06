class TileError(Exception):
    pass


class TileManager:
    def __init__(self, game):
        self.game = game

    def int_to_tile(self, val):
        return self.game.console.get_tile(val)

    def get_current_player(self):
        return self.game.console.get_current_player()

    def get_current_tile(self):
        return self.game.console.get_current_tile()

    def buy(self):
        try:
            current_tile = self.get_current_tile()
            current_player = self.get_current_player()
            current_tile.buy(current_player)
        except AttributeError:
            raise TileError("Tile is not a property!")

    def buy_house(self, tile):
        try:
            current_player = self.get_current_player()
            tile = self.int_to_tile(tile)
            tile.buy_house(current_player)
        except AttributeError:
            raise TileError("Tile is not an improvable tile!")

    def sell_house(self, tile):
        try:
            current_player = self.get_current_player()
            tile = self.int_to_tile(tile)
            tile.sell_house(current_player)
        except AttributeError:
            raise TileError("Tile is not an improvable tile!")

    def mortgage(self, tile):
        try:
            current_player = self.get_current_player()
            tile = self.int_to_tile(tile)
            tile.take_mortgage(current_player)
        except AttributeError:
            raise TileError("Tile is not a property!")

    def repay(self, tile):
        try:
            current_player = self.get_current_player()
            tile = self.int_to_tile(tile)
            tile.pay_mortgage(current_player)
        except AttributeError:
            raise TileError("Tile is not a property!")
