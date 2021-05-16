from Tiles.Property import Property


class Train(Property):
    def __init__(self, name, group=None):
        super().__init__(name, 200, 100, group)

    def rent(self, dice):
        return 25  # 50, 100, 200
