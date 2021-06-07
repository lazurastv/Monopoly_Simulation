class Tile:
    def __init__(self, pos):
        self.position = pos

    def __str__(self):
        return str(self.position)

    def copy(self, game):
        return Tile(self.position)

    def starting_from_event(self, player, dice):
        player.move(dice.value())

    def landed_on_event(self, player, dice):
        pass
