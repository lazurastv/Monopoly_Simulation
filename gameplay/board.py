import json
from pathlib import Path

from data.file_loader import FileLoader
from tiles.gotojail import GoToJail
from tiles.group import load_groups
from tiles.jail import Jail
from tiles.railroad import Train
from tiles.utility import Works
from tiles.hotel import Hotel
from tiles.tax import Tax
from tiles.tile import Tile


def load_mapping():
    with open(Path(__file__).parent / "../data/tile_indices.json") as mapping:
        return json.load(mapping)


class Board:
    def __init__(self):
        self.tiles = list(range(40))
        self.tile_mapping = load_mapping()
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
                loaded_tile = tile_type(**p["args"])
                self.tiles[self.tile_mapping[loaded_tile.name]] = loaded_tile

    def load_jail_tiles(self):
        jail_tile = Jail(self.tile_mapping["Jail"])
        self.tiles[self.tile_mapping["Jail"]] = jail_tile
        self.tiles[self.tile_mapping["Go To Jail"]] = GoToJail(jail_tile)

    def load_from_players(self, players):
        for player in players:
            for owned in player.properties:
                self.tiles[self.get(owned.name)] = owned
        # load_groups?

    def get(self, item):
        try:
            return self.tiles[item]
        except TypeError:
            return self.tiles[self.index_of(item)]

    def index_of(self, name):
        try:
            return self.tile_mapping[name]
        except IndexError:
            print("Such a tile does not exist!")

    def get_nearest(self, player, datatype):
        index = player.position
        indices = []
        data = FileLoader().get(datatype)
        tiles = data["tiles"]
        for tile in tiles:
            name = tile["args"]["name"]
            indices.append(self.tile_mapping[name])
        target = 40
        if max(indices) < index:
            index = 0
        for ind in indices:
            diff = ind - index
            if 0 < diff < target:
                target = ind
        return target
