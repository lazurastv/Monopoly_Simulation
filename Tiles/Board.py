import json

from Player import Player
from Tiles.Works import Works
from Tiles.Hotel import Hotel
from Tiles.Tax import Tax
from Tiles.Tile import Tile


class Board:
    def __init__(self, *, player_count=4, starting_money=1500, players=None):
        self.tiles = {}
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
        else:
            pass

    def load_tiles(self):
        self.load(Tile, "empty_tiles")
        self.load(Tax, "tax_tiles")
        self.load(Works, "work_tiles")

    def load(self, tile_type, file):
        with open("../Data/" + file + ".json") as data_file:
            data = json.load(data_file)
            for p in data["tiles"]:
                if p["index"] in self.tiles.keys():
                    print("Warning! Same key for", self.tiles[p["index"]].name, "and", p["args"]["name"])
                self.tiles[p["index"]] = tile_type(**p["args"])


board = Board(player_count=4, starting_money=1500)
print(sorted(board.tiles.keys()))
