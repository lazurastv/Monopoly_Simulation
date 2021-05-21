def parse(text):
    words = text.split()
    command = words[0]
    args = words[1:]
    for i in range(len(args)):
        try:
            args[i] = int(args[i])
        except ValueError:
            continue
    return command, args


class Auction:
    def __init__(self, players):
        self.players = players.copy()
        self.value = 0

    def auction(self):
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
                return self.players.get(0), self.value
            else:
                current_player += 1
                current_player %= player_count

    def run(self, command, args, player):
        if command == "bet":
            self.bet(*args)
        elif command == "end":
            self.end(player)
        else:
            print("Wrong command!")

    def bet(self, amount):
        if self.value >= amount:
            print("Bet must be greater than current bet!")
        else:
            self.value = amount

    def end(self, player):
        self.players.remove(player)
