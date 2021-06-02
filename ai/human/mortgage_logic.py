from ai.human.house_destroyer import HouseDestroyer
from ai.human.sub_logic import SubLogic


class MortgageLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)
        self.single_tiles = []
        self.groups = []

    def load_properties(self):
        properties = self.get_properties()
        for tile in properties:
            group = tile.group
            if group.has_houses():
                self.groups.append(group)
            elif not tile.mortgaged:
                self.single_tiles.append(tile)
        self.single_tiles.sort(key=lambda x: x.rent())
        self.groups.sort(key=lambda x: x.total_rent())

    def mortgage_single_tile(self):
        tile = self.single_tiles.pop(0)
        self.run("mortgage " + str(tile.position))

    def has_single_tile(self):
        return len(self.single_tiles) > 0

    def destroy_house(self, target):
        self.run("destroy " + str(target.position))

    def destroy_current_group(self):
        group = self.groups.pop(0)
        for tile in group:
            self.single_tiles.append(tile)

    def has_houses(self):
        return len(self.groups) > 0

    def in_debt(self):
        player = self.get_player()
        return not player.positive_balance()

    def get_properties(self):
        player = self.get_player()
        return player.properties

    def keep_alive(self):
        house_destroyer = HouseDestroyer()
        self.load_properties()
        while self.in_debt():
            if self.has_single_tile():
                self.mortgage_single_tile()
            elif self.has_houses():
                group = self.groups[0]
                house_destroyer.load_group(group)
                if house_destroyer.has_houses():
                    target = house_destroyer.next_house()
                    self.destroy_house(target)
                else:
                    self.destroy_current_group()
            else:
                return
