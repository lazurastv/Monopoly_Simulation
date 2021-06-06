from copy import deepcopy

from gamecode.control.parser import Parser


class AuctionError(Exception):
    pass


class Auction:
    def __init__(self, game):
        self.game = game
        self.value = 0
        self.running = False
        self.players = None
        self.current_player_id = None
        commands = {
            "bet": self.bet,
            "val": self.current_value,
            "end": self.end
        }
        self.parser = Parser(commands)

    def start(self):
        if self.game.console.current_tile_owned():
            raise AuctionError("Tile cannot be auctioned!")
        else:
            self.value = 0
            self.players = deepcopy(self.game.players)
            self.current_player_id = self.game.console.turn_mgr.current_player_id
            self.running = True
            while self.running:
                self.get_current_player().play()

    def run(self, text):
        self.parser.parse_input(text)
        if self.players.count() == 1:
            self.finish()

    def finish(self):
        self.game.console.get_current_tile().buy(self.get_current_player(), self.value)
        self.running = False

    def bet(self, amount):
        player = self.get_current_player()
        if self.value >= amount:
            raise AuctionError("Bet must be greater than current bet!")
        elif not player.has(amount):
            raise AuctionError("You don't have this much!")
        else:
            self.value = amount
            self.next()

    def current_value(self):
        print(self.value)

    def end(self):
        self.players.remove(self.get_current_player())
        self.next()

    def next(self):
        self.current_player_id += 1
        self.current_player_id %= self.players.count()

    def get_current_player(self):
        return self.players.get(self.current_player_id)
