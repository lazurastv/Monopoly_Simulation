from gamecode.gameplay.player import Player


class PlayersError(Exception):
    pass


class Players:
    def __init__(self, starting_money, amount):
        self.players = []
        for i in range(amount):
            self.players.append(Player(i, starting_money))

    def __iter__(self):
        return iter(self.players)

    def inject_logic(self, logic):
        for i in range(self.count()):
            self.players[i].inject_logic(logic[i])

    def earn(self, amount, player):
        for p in self.players:
            if p != player:
                p.pay(amount, player)

    def pay(self, amount, player):
        for p in self.players:
            if p != player:
                player.pay(amount, p)

    def get(self, index):
        try:
            return self.players[index]
        except IndexError:
            raise PlayersError("Player doesn't exist!")

    def get_by_id(self, index):
        for player in self:
            if player.id == index:
                return player

    def fill_unrolled_graph(self, unrolled_graph):
        filled_graph = []
        for owner, tile in unrolled_graph:
            filled_graph.append((self.get_by_id(owner), tile))
        return filled_graph

    def count(self):
        return len(self.players)

    def remove(self, player):
        self.players.remove(player)

    def kill(self, player: Player):
        self.remove(player)
        player.kill()
