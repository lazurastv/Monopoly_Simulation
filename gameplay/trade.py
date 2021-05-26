class TradeException(Exception):
    pass


class Trade:
    def __init__(self, player_1, player_2, amount_1_to_2, tiles):
        self.player_1 = player_1
        self.player_2 = player_2
        self.diff = amount_1_to_2
        self.tiles = tiles
        self.verify()

    def verify(self):
        if self.diff > 0 and not self.player_1.has(self.diff):
            print()
            raise TradeException(str(self.player_1) + " lacks the necessary funds!")
        elif self.diff < 0 and not self.player_2.has(self.diff):
            raise TradeException(str(self.player_2) + " lacks the necessary funds!")
        else:
            for tile in self.tiles:
                try:
                    if tile.owner != self.player_1 and tile.owner != self.player_2:
                        raise TradeException(str(tile) + " doesn't belong to either player!")
                except AttributeError:
                    raise TradeException(str(tile) + " is not tradeable!")

    def accept(self):
        # Note: Anyone can accept trades, since the console input is based on trust anyways
        if self.diff > 0:
            self.player_1.pay(self.diff, self.player_2)
        else:
            self.player_2.pay(self.diff, self.player_1)
        for tile in self.tiles:
            if tile.owner == self.player_1:
                tile.change_owner(self.player_2)
            else:
                tile.change_owner(self.player_1)
