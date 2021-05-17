class Tile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def starting_from_event(self, player, dice):
        start = player.position
        player.move(dice.value)
        if start > player.position:
            player.earn(200)
        self.board.get_index(player.position).landed_on_event()

    def landed_on_event(self, player, dice):
        pass
