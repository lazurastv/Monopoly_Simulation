from gamecode.tiles.tile import Tile


class GoToJail(Tile):
    def __init__(self, pos, jail):
        super().__init__(pos)
        self.jail = jail

    def __str__(self):
        return "Go To Jail"

    def copy(self, jail):
        return GoToJail(self.position, jail)

    def landed_on_event(self, player, dice):
        self.jail.put_in_jail(player)
