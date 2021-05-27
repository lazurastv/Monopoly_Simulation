class TileManager:
    def __init__(self, turn_mgr, info):
        self.turn_mgr = turn_mgr
        self.info = info

    def int_to_tile(self, val):
        return self.info.get_tile(val)

    def buy(self):
        try:
            current_tile = self.turn_mgr.get_current_tile()
            current_player = self.turn_mgr.get_current_player()
            current_tile.buy(current_player)
        except AttributeError:
            print("Tile is not a property!")

    def buy_house(self, tile):
        try:
            current_player = self.turn_mgr.get_current_player()
            tile = self.int_to_tile(tile)
            tile.buy_house(current_player)
        except AttributeError:
            print("Tile is not an improvable tile!")

    def sell_house(self, tile):
        try:
            current_player = self.turn_mgr.get_current_player()
            tile = self.int_to_tile(tile)
            tile.sell_house(current_player)
        except AttributeError:
            print("Tile is not an improvable tile!")

    def mortgage(self, tile):
        try:
            current_player = self.turn_mgr.get_current_player()
            tile = self.int_to_tile(tile)
            tile.take_mortgage(current_player)
        except AttributeError:
            print("Tile is not a property!")

    def repay(self, tile):
        try:
            current_player = self.turn_mgr.get_current_player()
            tile = self.int_to_tile(tile)
            tile.pay_mortgage(current_player)
        except AttributeError:
            print("Tile is not a property!")
