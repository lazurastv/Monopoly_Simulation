class Information:
    def __init__(self, game):
        self.game = game

    def get_player(self, player):
        return self.game.get_player_by_id(player)

    def get_player_count(self):
        return self.game.get_player_count()

    def get_tile(self, tile):
        return self.game.get_tile(tile)

    def info_player(self, player):
        print(self.get_player(player))

    def info_tile(self, tile):
        print(self.get_tile(tile))
