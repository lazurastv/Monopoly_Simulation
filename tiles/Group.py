import json
from pathlib import Path


class Group:
    def __init__(self, *properties):
        self.tiles = [*properties]

    def __str__(self):
        return str([x.name for x in self.tiles])

    def count(self, player):
        owns = [player.has_tile(x) and not x.mortgaged for x in self.tiles]
        return owns.count(True)

    def full_set(self, player):
        return self.count(player) == len(self.tiles)

    def has_houses(self):
        return self.highest_house() != 0

    def highest_house(self):
        return max([x.houses for x in self.tiles])

    def lowest_house(self):
        return min([x.houses for x in self.tiles])


def load_groups(board):
    with open(Path(__file__).parent / "../data/groups.json")\
            as group_file:
        data = json.load(group_file)
        for indexes in data["groups"]:
            group = Group(*[board.get(index) for index in indexes["members"]])
            for index in indexes["members"]:
                board.get(index).group = group