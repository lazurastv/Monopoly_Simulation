import json
from pathlib import Path

from tiles.goToJail import GoToJail
from tiles.group import load_groups
from tiles.jail import Jail
from tiles.train import Train
from tiles.works import Works
from tiles.hotel import Hotel
from tiles.tax import Tax
from tiles.tile import Tile


class Board:
    def __init__(self):
        self.tiles = list(range(40))
        self.tile_mapping = {}
        self.load_tiles()
        load_groups(self)

    def load_tiles(self):
        self.load(Tile, "empty")
        self.load(Tax, "tax")
        self.load(Works, "work")
        self.load(Train, "train")
        self.load(Hotel, "hotel")
        self.load_jail_tiles()

    def load(self, tile_type, file):
        filename = "../data/" + file + "_tiles.json"
        with open(Path(__file__).parent / filename) as data_file:
            data = json.load(data_file)
            for p in data["tiles"]:
                index = p["index"]
                loaded_tile = tile_type(**p["args"])
                self.tiles[index] = loaded_tile
                self.tile_mapping[loaded_tile.name] = index

    def load_jail_tiles(self):
        jail_tile = Jail(10)
        self.tiles[10] = jail_tile
        self.tiles[30] = GoToJail(jail_tile)

    def load_from_players(self, players):
        for player in players:
            for owned in player.properties:
                self.tiles[self.get(owned.name)] = owned
        # load_groups?

    def get(self, item):
        try:
            return self.tiles[item]
        except IndexError:
            return self.tiles[self.index_of(item)]

    def index_of(self, name):
        return self.tile_mapping[name]
