from Player import Player
from Players import Players
from Tiles.Board import Board


class Game:
    def __init__(self, start_money=1500, player_count=4, players=None):
        self.board = Board()
        self.players = Players()
        if players:
            self.players = players
            self.player_count = len(self.players)
            self.board.load_from_players(self.players)

    def create_new_game(self, start_money, player_count):
        players = []
        for i in range(player_count):
            players.append(Player(i, start_money, 0, self))
        self.__init__(players)

    def get_player(self, index):
        return self.players[index]

    def get_tile(self, tile):
        return self.board.get(tile)
