import json


class Group:
    def __init__(self, *properties):
        self.tiles = [*properties]

    def count(self, player):
        owns = [player.has(x) and not x.mortgaged() for x in self.tiles]
        return owns.count(True)

    def full_set(self, player):
        return self.count(player) == len(self.tiles)

    def has_houses(self):
        return [x.houses > 0 for x in self.tiles].count(True) > 0


def load_groups(board):
    with open("../Data/groups.json") as group_file:
        data = json.load(group_file)
        for indexes in data["groups"]:
            group = Group(*[board.get_index(index) for index in indexes])
            for index in indexes:
                board.get_index(index).set_group(group)
