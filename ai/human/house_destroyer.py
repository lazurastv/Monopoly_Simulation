class HouseDestroyer:
    def __init__(self):
        self.group = None
        self.index = -1
        self.length = 0

    def load_group(self, group):
        if self.group is not group:
            self.group = group
            self.index = -1
            self.length = len(group)

    def next_house(self):
        self.index += 1
        self.index %= self.length
        return self.group[self.index]

    def has_houses(self):
        try:
            return self.group.has_houses()
        except AttributeError:
            return False
