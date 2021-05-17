from Tiles.Tile import Tile


class GoToJail(Tile):
    def __init__(self, jail):
        super().__init__("Go to Jail")
        self.jail = jail

    def landed_on_event(self, player, dice):
        self.jail.put_in_jail(player)
