from ai.human.sub_logic import SubLogic
from gamecode.tiles.hotel import HouseError


class TileLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)

    def manage_tiles(self):
        player = self.get_player()
        properties = player.properties.copy()
        index = 0
        while len(properties) > 0:
            tile = properties[index]
            try:
                self.run("build " + str(tile.position))
            except HouseError:
                pass

