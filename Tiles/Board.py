import json

from Tiles.GoToJail import GoToJail
from Tiles.Group import load_groups
from Tiles.Jail import Jail
from Tiles.Train import Train
from Tiles.Works import Works
from Tiles.Hotel import Hotel
from Tiles.Tax import Tax
from Tiles.Tile import Tile


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
        with open("../Data/" + file + "_tiles.json") as data_file:
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

    def get(self, tile):
        if tile is int:
            return self.tiles[tile]
        elif tile is str:
            return self.tiles[self.index_of(tile)]

    def index_of(self, name):
        return self.tile_mapping[name]
