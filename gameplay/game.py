from control.console import Console
from gameplay.players import Players
from gameplay.board import Board


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
        return self.players.get(index)

    def get_player_count(self):
        return self.players.count()

    def get_tile(self, tile):
        return self.board.get(tile)

    def start(self):
        self.console.get_player_input()
