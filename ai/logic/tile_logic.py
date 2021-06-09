from ai.logic.sub_logic import SubLogic
from gamecode.tiles.hotel import Hotel, HouseError
from gamecode.tiles.property import MortgageError


class TileLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)

    def build_hotels(self, properties):
        improvable = []
        for tile in properties:
            if isinstance(tile, Hotel) and tile.group.owned() and not tile.has_hotel():
                improvable.append(tile)
        for tile in improvable:
            properties.remove(tile)
        self.improve(improvable)

    def improve(self, improvable):
        improvable.sort(key=lambda x: x.derivative(), reverse=True)
        index = 0
        while len(improvable) > 0:
            hotel = improvable[index]
            if hotel.group.pay_all_mortgage_cost() > 0:
                self.repay_mortgages(hotel.group)
            elif hotel.has_hotel():
                improvable.pop(index)
            elif not hotel.even():
                index += 1
            else:
                self.run("build " + str(hotel.position))
                improvable.sort(key=lambda x: x.derivative(), reverse=True)
                index = 0

    def repay_mortgages(self, properties):
        for tile in properties:
            if tile.mortgaged:
                self.run("repay " + str(tile.position))

    def manage_tiles(self):
        properties = self.get_properties().copy()
        try:
            self.build_hotels(properties)
            self.repay_mortgages(properties)
        except (MortgageError, HouseError):
            return
