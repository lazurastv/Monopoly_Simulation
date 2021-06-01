from gamecode.tiles.group import Group
from gamecode.tiles.property import Property


class MortgageLogic:
    def __init__(self, logic):
        self.logic = logic
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
        self.single_tiles.sort(key=Property.rent)
        self.groups.sort(key=Group.total_rent)

    def mortgage_non_complete_groups(self):
        for tile in self.single_tiles:
            if not self.in_debt():
                return
            else:
                self.run("mortgage " + str(tile.position))

    def destroy_houses(self):
        for group in self.groups:
            while group.has_houses():
                for tile in group:
                    if not self.in_debt():
                        return
                    else:
                        self.run("destroy " + str(tile.position))

    def mortgage_rest(self):
        for group in self.groups:
            for tile in group:
                if not self.in_debt():
                    return
                else:
                    self.run("mortgage " + str(tile.position))

    def in_debt(self):
        player = self.get_player()
        return not player.positive_balance()

    def get_properties(self):
        player = self.get_player()
        return player.properties

    def get_player(self):
        return self.logic.player

    def run(self, text):
        self.logic.run(text)

    def keep_alive(self):
        self.load_properties()
        self.mortgage_non_complete_groups()
        self.destroy_houses()
        self.mortgage_rest()
