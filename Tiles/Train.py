from Tiles.Property import Property


class Train(Property):
    def __init__(self, name, group):
        super().__init__(name, 200, 100, group)

    def rent(self, dice):
        val = self.group.count(self.owner)
        if val == 1:
            return 25
        if val == 2:
            return 50
        if val == 3:
            return 100
        if val == 4:
            return 200
        else:
            raise Exception("Error! Group count evaluated to " + val)
