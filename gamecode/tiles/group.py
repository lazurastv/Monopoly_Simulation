from gamecode.data.file_loader import FileLoader


class Group:
    def __init__(self, name, *properties):
        self.name = name
        self.tiles = [*properties]

    def __str__(self):
        return str([x.position for x in self.tiles])

    def __iter__(self):
        return iter(self.tiles)

    def __len__(self):
        return len(self.tiles)

    def __getitem__(self, item):
        return self.tiles[item]

    def count_owned_and_not_mortgaged(self, player):
        owns = [player.has(x) and not x.mortgaged for x in self]
        return owns.count(True)

    def count_owned(self, player):
        owns = [player.has(x) for x in self]
        return owns.count(True)

    def max_ownership(self, players):
        return max([self.count_owned_and_not_mortgaged(x) for x in players])

    def owners(self):
        owner_list = set()
        for tile in self:
            if tile.owner is not None:
                owner_list.add(tile.owner)
        return owner_list

    def owned_by(self, player):
        return self.count_owned(player) == len(self)

    def owned_and_not_mortgaged(self, player):
        return self.count_owned_and_not_mortgaged(player) == len(self)

    def filled(self):
        for tile in self:
            if tile.owner is None:
                return False
        return True

    def owned(self):
        return self.filled() and len(self.owners()) == 1

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
            return [0]

    def pay_all_mortgage_cost(self):
        cost = 0
        for tile in self:
            if tile.mortgaged:
                cost += tile.pay_mortgage_cost()
        return cost

    def derivative(self):
        dfxs = [x.derivative() for x in self]
        max_dfx = max(dfxs)
        return max_dfx, dfxs.index(max_dfx)


def load_groups(board):
    data = FileLoader().get("Group")
    for indexes in data:
        group = Group(indexes["name"], *[board.get(index) for index in indexes["members"]])
        for index in indexes["members"]:
            board.get(index).group = group
