from control.parser import parse


class Auction:
    def __init__(self, tile, players):
        self.tile = tile
        self.players = players.__copy__()
        self.current_player = 0
        self.value = 0

    def verify_correctness(self):
        try:
            return not self.tile.owned()
        except AttributeError:
            return False

    def start(self):
        if not self.verify_correctness():
            print("Tile cannot be auctioned!")
            return
        self.current_player = 0
        while True:
            player_count = self.players.count()
            if player_count == 1:
                self.finish()
                return
            print("Current bet:", self.value)
            command, _ = parse(input())
            try:
                self.run(command, self.players.get(self.current_player))
            except TypeError:
                print("Wrong argument count!")
            except ValueError:
                print("Wrong arguments!")
            new_count = self.players.count()
            if player_count == new_count:
                self.current_player += 1
            if self.current_player >= new_count:
                self.current_player = 0
                for player in self.players:
                    if not player.has(self.value):
                        self.end(player)

    def finish(self):
        self.tile.buy(self.players.get(0), self.value)

    def run(self, command, player):
        if command == "end":
            self.end(player)
            return
        try:
            self.bet(player, command)
        except ValueError:
            print("Error! Type number or end.")

    def bet(self, player, amount):
        if self.value >= amount:
            print("Bet must be greater than current bet!")
        elif not player.has(amount):
            print("You don't have this much!")
        else:
            self.value = amount

    def end(self, player):
        self.players.remove(player)
