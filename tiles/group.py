from data.file_loader import FileLoader


class Group:
    def __init__(self, *properties):
        self.tiles = [*properties]

    def __str__(self):
        return str([x.position for x in self.tiles])

    def count(self, player):
        owns = [player.has(x) and not x.mortgaged for x in self.tiles]
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
    data = FileLoader().get("Group")
    for indexes in data:
        group = Group(*[board.get(index) for index in indexes["members"]])
        for index in indexes["members"]:
            board.get(index).group = group
