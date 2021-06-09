from ai.logic.sub_logic import SubLogic


class MortgageLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)
        self.single_tiles = []
        self.improved_tiles = []

    def load_properties(self):
        self.single_tiles = []
        self.improved_tiles = []
        player = self.logic.player
        properties = self.get_properties()
        for tile in properties:
            if tile.group.owned_and_not_mortgaged(player) and tile.group.highest_house() > 0:
                self.improved_tiles.append(tile)
            elif not tile.mortgaged:
                self.single_tiles.append(tile)
        self.single_tiles.sort(key=lambda x: x.rent())

    def mortgage_single_tile(self):
        tile = self.single_tiles.pop(0)
        self.run("mortgage " + str(tile.position))

    def has_single_tile(self):
        return len(self.single_tiles) > 0

    def destroy_house(self, target):
        self.run("destroy " + str(target.position))

    def destroy_group(self, group):
        for tile in group:
            self.single_tiles.append(tile)
            self.improved_tiles.remove(tile)

    def has_improved_tiles(self):
        return len(self.improved_tiles) > 0

    def in_debt(self):
        player = self.get_player()
        return not player.positive_balance()

    def sell_house(self):
        self.improved_tiles.sort(key=lambda x: x.derivative(True))
        index = 0
        tile = self.improved_tiles[index]
        while tile.houses == 0 or not tile.even(True):
            index += 1
            tile = self.improved_tiles[index]
        self.run("destroy " + str(tile.position))
        if tile.group.highest_house() == 0:
            self.destroy_group(tile.group)

    def keep_alive(self):
        self.load_properties()
        while self.in_debt():
            if self.has_single_tile():
                self.mortgage_single_tile()
            elif self.has_improved_tiles():
                self.sell_house()
            else:
                return
