from game.control.parser import Parser


class Auction:
    def __init__(self, turn_mgr, players):
        self.turn_mgr = turn_mgr
        self.players = players
        self.players_copy = players.__deepcopy__()
        self.current_player_id = 0
        self.value = 0
        self.running = False
        commands = {
            "bet": self.bet,
            "end": self.end
        }
        self.parser = Parser(commands)

    def start(self):
        if self.turn_mgr.current_tile_owned():
            print("Tile cannot be auctioned!")
        else:
            self.running = True

    def run(self, text):
        self.parser.parse_input(text)
        if self.players_copy.count() == 1:
            self.finish()

    def finish(self):
        self.turn_mgr.get_current_tile().buy(self.players_copy.get(0), self.value)
        self.current_player_id = 0
        self.value = 0
        self.players_copy = self.players.__deepcopy__()
        self.running = False

    def bet(self, amount):
        player = self.players_copy.get(self.current_player_id)
        if self.value >= amount:
            print("Bet must be greater than current bet!")
        elif not player.has(amount):
            print("You don't have this much!")
        else:
            self.value = amount
            self.next()

    def end(self, player):
        self.players_copy.remove(player)
        self.next()

    def next(self):
        self.current_player_id += 1
        self.current_player_id %= self.players_copy.count()
