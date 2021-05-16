import json

from Player import Player
from Tiles.Train import Train
from Tiles.Works import Works
from Tiles.Hotel import Hotel
from Tiles.Tax import Tax
from Tiles.Tile import Tile


class Board:
    def __init__(self, *, player_count=4, starting_money=1500, players=None):
        self.tiles = list(range(40))
        self.tile_mapping = {}
        self.load_tiles()
        if players:
            self.players = players
        else:
            self.players = []
            self.load_standard_players(player_count, starting_money)

    def load_standard_players(self, player_count, starting_money):
        if player_count > 0:
            for i in range(player_count):
                self.players.append(Player(starting_money, 0, [], False))

    def load_tiles(self):
        self.load(Tile, "empty")
        self.load(Tax, "tax")
        self.load(Works, "work")
        self.load(Train, "train")
        self.load(Hotel, "hotel")

    def load(self, tile_type, file):
        with open("../Data/" + file + "_tiles.json") as data_file:
            data = json.load(data_file)
            for p in data["tiles"]:
                index = p["index"]
                tile = tile_type(**p["args"], board=self)
                self.tiles[index] = tile
                self.tile_mapping[tile.name] = index

    def get_index(self, index):
        return self.tiles[index]

    def index_of(self, name):
        return self.tile_mapping[name]


board = Board(player_count=4, starting_money=1500)
for tile in board.tiles:
    print(tile)