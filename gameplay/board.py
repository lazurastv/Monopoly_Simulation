import json
from pathlib import Path

from cards.deck import Deck
from data.file_loader import FileLoader
from tiles.cardtile import CardTile
from tiles.gotojail import GoToJail
from tiles.group import load_groups
from tiles.jail import Jail
from tiles.railroad import Train
from tiles.utility import Utility
from tiles.hotel import Hotel
from tiles.tax import Tax
from tiles.tile import Tile


def load_mapping():
    with open(Path(__file__).parent / "../data/tile_indices.json") as mapping:
        return json.load(mapping)


class Board:
    def __init__(self, game):
        self.tiles = list(range(40))
        self.tile_mapping = FileLoader().get("Layout")
        self.load_tiles(game)
        load_groups(self)

    def load_tiles(self, game):
        self.load(Tile, "Empty")
        self.load(Tax, "Tax")
        self.load(Utility, "Utility")
        self.load(Train, "Railroad")
        self.load(Hotel, "Hotel")
        self.load_jail_tiles()
        self.load_card_tiles(game)

    def load(self, tile_type, datatype):
        data = FileLoader().get(datatype)
        for p in data:
            name = p["name"]
            p.pop("name")
            p["pos"] = self.tile_mapping[name]
            loaded_tile = tile_type(**p)
            self.tiles[loaded_tile.position] = loaded_tile

    def load_jail_tiles(self):
        jail_index = self.tile_mapping["Jail"]
        go_to_jail_index = self.tile_mapping["Go To Jail"]
        jail_tile = Jail(jail_index)
        self.tiles[jail_index] = jail_tile
        self.tiles[go_to_jail_index] = GoToJail(go_to_jail_index, jail_tile)

    def load_card_tiles(self, game):
        self.load_card_tiles_type("Community", game)
        self.load_card_tiles_type("Chance", game)

    def load_card_tiles_type(self, cardtype, game):
        deck = Deck(cardtype)
        indices = self.tile_mapping[cardtype]
        for index in indices:
            self.tiles[index] = CardTile(index, deck, game)

    def get(self, item):
        try:
            return self.tiles[item]
        except TypeError:
            return self.tiles[self.index_of(item)]

    def index_of(self, name):
        try:
            return self.tile_mapping[name]
        except KeyError:
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
