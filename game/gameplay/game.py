from game.control.console import Console
from game.gameplay.players import Players
from game.gameplay.board import Board


class Game:
    def __init__(self, start_money=1500, player_count=4):
        self.board = Board(self)
        self.players = Players(start_money, player_count)
        self.console = Console(self)

    def get_player(self, index):
        return self.players.get(index)

    def get_player_count(self):
        return self.players.count()

    def get_tile(self, tile):
        return self.board.get(tile)

    def get_nearest(self, player, filename):
        return self.board.get_nearest(player, filename)

    def start(self):
        while True:
            self.console.run(input())
