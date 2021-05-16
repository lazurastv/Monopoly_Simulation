from Tiles.Tile import Tile


class GoToJail(Tile):
    def __init__(self, board):
        super().__init__("Go to Jail", board)

    def landed_on_event(self, player, dice):
        self.board.index_of("Jail").put_in_jail(player)
