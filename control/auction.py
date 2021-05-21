from control.parser import parse


class Auction:
    def __init__(self, tile, players):
        self.tile = tile
        self.players = players.copy()
        self.value = 0

    def start(self):
        current_player = 0
        while True:
            print("Current bet:", self.value)
            command, args = parse(input())
            try:
                self.run(command, args, self.players.get(current_player))
            except TypeError:
                print("Wrong argument count!")
            except ValueError:
                print("Wrong arguments!")
            player_count = self.players.count()
            if player_count == 1:
                self.finish()
                return
            else:
                current_player += 1
                if current_player == player_count:
                    current_player = 0
                    for player in self.players:
                        if not player.has_money(self.value):
                            self.players.remove(player)

    def finish(self):
        self.tile.buy(self.players.get(0), self.value)

    def run(self, command, args, player):
        if command == "bet":
            self.bet(player, *args)
        elif command == "end":
            self.end(player)
        else:
            print("Wrong command!")

    def bet(self, player, amount):
        if self.value >= amount:
            print("Bet must be greater than current bet!")
        elif not player.has_money(amount):
            print("You don't have this much!")
        else:
            self.value = amount

    def end(self, player):
        self.players.remove(player)
