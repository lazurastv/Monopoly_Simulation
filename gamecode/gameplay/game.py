from ai.human.human_logic import HumanLogic
from ai.human.manual_logic import ManualLogic
from gamecode.control.console import Console
from gamecode.gameplay.players import Players
from gamecode.gameplay.board import Board


class Game:
    def __init__(self, start_money=1500, player_count=4):
        self.players = []
        self.board = Board(self)
        self.console = Console(self)
        self.players = Players(start_money, player_count)
        logic = [ManualLogic(self), HumanLogic(self, 1), HumanLogic(self, 2), HumanLogic(self, 3)]
        self.players.inject_logic(logic)

    def get_groups(self):
        groups = set()
        for tile in self.board:
            try:
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
        while True:
            player = self.console.get_current_player()
            player.play()
