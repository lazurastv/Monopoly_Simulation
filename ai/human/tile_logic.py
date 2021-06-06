from ai.human.sub_logic import SubLogic
from gamecode.tiles.hotel import HouseError, Hotel
from gamecode.tiles.property import MortgageError


class TileLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)

    def build_hotels(self, properties):
        groups = []
        remove = []
        for tile in properties:
            if isinstance(tile, Hotel) and tile.group not in groups:
                groups.append(tile.group)
                remove.append(tile)
        for tile in remove:
            properties.remove(tile)
        groups.sort(key=lambda x: x.rent_derivative(), reverse=True)
        for group in groups:
            self.improve_group(group)

    def improve_group(self, group):
        for tile in group:
            if tile.mortgaged:
                self.run("repay " + str(tile.position))
        failed = [False for _ in group]
        while False in failed:
            for i, tile in enumerate(group):
                try:
                    self.run("build " + str(tile.position))
                    failed[i] = False
                except HouseError:
                    failed[i] = True
        for tile in group:
            if tile.houses != 5:
                raise HouseError

    def repay_mortgages(self, properties):
        for tile in properties:
            if tile.mortgaged:
                self.run("repay " + str(tile.position))

    def manage_tiles(self):
        player = self.get_player()
        properties = player.properties.copy()
        try:
            self.build_hotels(properties)
            self.repay_mortgages(properties)
        except (MortgageError, HouseError):
            pass
