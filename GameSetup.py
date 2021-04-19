from Console import Console
from Player import Player
from utilities import shuffle


class GameSetup:
    def __init__(self):
        self.players = []
        self.starting_money = 2000
        keywords = {
            "add": (self.add_players, "int"),
            "set": (self.set_starting_money, "int"),
            "run": (self.finished)
        }
        self.console = Console(keywords)

    def add_player(self):
        self.players.append(Player())

    def add_players(self, count):
        for i in range(count):
            self.add_player()

    def set_starting_money(self, value):
        self.starting_money = value

    def give_starting_money(self):
        for player in self.players:
            player.earn(self.starting_money)

    def finished(self):
        self.give_starting_money()
        shuffle(self.players)