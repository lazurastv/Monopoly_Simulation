from gamecode.data.file_loader import FileLoader


class Group:
    def __init__(self, name, *properties):
        self.name = name
        self.tiles = [*properties]

    def __str__(self):
        return str([x.position for x in self.tiles])

    def __iter__(self):
        return iter(self.tiles)

    def count(self, player):
        owns = [player.has(x) and not x.mortgaged for x in self]
        return owns.count(True)

    def max_ownership(self, players):
        return max([self.count(x) for x in players])

    def total(self):
        return len(self.tiles)

    def owners(self):
        owner_list = set()
        for tile in self:
            if tile.owner is not None:
                owner_list.add(tile.owner)
        return owner_list

    def full_set(self, player):
        return self.count(player) == self.total()

    def filled(self):
        for tile in self:
            if tile.owner is None:
                return False
        return True

    def has_houses(self):
        return self.highest_house() != 0

    def highest_house(self):
        return max(self.get_house_count())

    def lowest_house(self):
        return min(self.get_house_count())

    def get_house_count(self):
        try:
            return [x.houses for x in self]
        except AttributeError:
            return 0

    def total_rent(self):
        rent_sum = 0
        for tile in self:
            rent_sum += tile.rent()
        return rent_sum


def load_groups(board):
    data = FileLoader().get("Group")
    for indexes in data:
        group = Group(indexes["name"], *[board.get(index) for index in indexes["members"]])
        for index in indexes["members"]:
            board.get(index).group = group
