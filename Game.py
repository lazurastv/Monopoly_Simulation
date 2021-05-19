from Console import Console
from Players import Players
from Tiles.Board import Board


class Game:
    def __init__(self, start_money=1500, player_count=4, players=None):
        self.board = Board()
        if players:
            self.players = players
            self.board.load_from_players(self.players)
        else:
            self.players = Players(start_money, player_count)
        self.console = Console(self)

    def get_player(self, index):
        return self.players[index]

    def get_tile(self, tile):
        return self.board.get(tile)
