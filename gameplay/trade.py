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
        if not self.player_1.has_money(self.diff) or not self.player_2.has_money(self.diff):
            raise TradeException("Insufficient funds for trade!")
        else:
            for tile in self.tiles:
                if tile.owner != self.player_1 and tile.owner != self.player_2:
                    raise TradeException(str(tile), "doesn't belong to either player!")

    def accept(self, player):
        if player != self.player_2:
            print("You cannot accept this trade!")
        elif self.diff > 0:
            self.player_1.pay(self.diff, self.player_2)
        else:
            self.player_2.pay(self.diff, self.player_1)
            for tile in self.tiles:
                if tile.owner == self.player_1:
                    tile.change_owner(self.player_2)
                else:
                    tile.change_owner(self.player_1)
