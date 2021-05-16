from Tiles.Property import Property


class Works(Property):
    def __init__(self, name, board, group=None):
        super().__init__(name, 150, 75, board)

    def rent(self, dice):
        return dice * 4  # 10 if both
