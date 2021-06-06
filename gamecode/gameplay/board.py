from gamecode.cards.deck import Deck
from gamecode.data.file_loader import FileLoader
from gamecode.tiles.cardtile import CardTile
from gamecode.tiles.gotojail import GoToJail
from gamecode.tiles.group import load_groups
from gamecode.tiles.jail import Jail
from gamecode.tiles.railroad import Train
from gamecode.tiles.utility import Utility
from gamecode.tiles.hotel import Hotel
from gamecode.tiles.tax import Tax
from gamecode.tiles.tile import Tile


class BoardError(Exception):
    pass


class Board:
    def __init__(self, game):
        self.tiles = list(range(40))
        self.tile_mapping = FileLoader().get("Layout")
        self.load_tiles(game)
        load_groups(self)

    def __iter__(self):
        return iter(self.tiles)

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
        except IndexError:
            raise BoardError("Such a tile does not exist!")

    def index_of(self, name):
        try:
            return self.tile_mapping[name]
        except KeyError:
            raise BoardError("Such a tile does not exist!")

    def get_nearest(self, player, datatype):
        index = player.position
        indices = []
        data = FileLoader().get(datatype)
        for tile in data:
            name = tile["name"]
            indices.append(self.tile_mapping[name])
        target = 40
        if max(indices) < index:
            index = 0
        for ind in indices:
            diff = ind - index
            if 0 < diff < target:
                target = ind
        return target
