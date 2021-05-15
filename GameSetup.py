from Player import Player
from utilities import shuffle
from utilities import force_type_input


class GameSetup:
    def __init__(self):
        self.players = []
        self.starting_money = 2000
        self.ask_for_player_count()
        self.ask_for_starting_money()
        self.finish()

    def ask_for_player_count(self):
        print("Input player count: ", end="")
        self.add_players(force_type_input(int))

    def ask_for_starting_money(self):
        print("Input starting money: ", end="")
        self.starting_money = force_type_input(int)

    def add_player(self):
        self.players.append(Player())

    def add_players(self, count):
        for i in range(count):
            self.add_player()

    def give_starting_money(self):
        for player in self.players:
            player.earn(self.starting_money)

    def finish(self):
        self.give_starting_money()
        shuffle(self.players)

    def __str__(self):
        return str(str(player) for player in self.players)
