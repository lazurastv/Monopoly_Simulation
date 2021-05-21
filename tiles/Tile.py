class Tile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def starting_from_event(self, player, dice):
        player.move(dice.value())

    def landed_on_event(self, player, dice):
        player.crossed_start_bonus()
