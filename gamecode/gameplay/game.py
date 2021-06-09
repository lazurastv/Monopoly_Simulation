from copy import deepcopy

from ai.logic.human_logic import HumanLogic
from gamecode.control.console import Console
from gamecode.gameplay.players import Players
from gamecode.gameplay.board import Board


class Game:
    def __init__(self, start_money=1500, player_count=4):
        self.board = Board(self)
        self.console = Console(self)
        self.players = Players(start_money, player_count)
        logic = [HumanLogic(self, 0), HumanLogic(self, 1), HumanLogic(self, 2), HumanLogic(self, 3)]
        self.players.inject_logic(logic)
        self.winner = None

    def copy(self):
        game_copy = Game()
        game_copy.players = deepcopy(self.players)
        game_copy.board = self.board.copy(game_copy)
        game_copy.console = self.console.copy(game_copy)
        logic = [x.logic.copy(game_copy) for x in self.players]
        game_copy.players.inject_logic(logic)
        return game_copy

    def get_groups(self, hotels_only=False):
        groups = set()
        for tile in self.board:
            try:
                group = tile.group
                if not hotels_only or (group.name != "utility" and group.name != "railroad"):
                    groups.add(tile.group)
            except AttributeError:
                continue
        return groups

    def get_player(self, index):
        return self.players.get(index)

    def get_player_count(self):
        return self.players.count()

    def get_tile(self, tile):
        return self.board.get(tile)

    def get_nearest(self, player, filename):
        return self.board.get_nearest(player, filename)

    def start(self):
        self.console.start()

    def end(self, player):
        self.winner = player.id
        self.console.end()
