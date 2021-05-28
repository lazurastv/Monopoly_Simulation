from ai.human.auction_logic import AuctionLogic
from ai.human.logic import Logic


class HumanLogic(Logic):
    def __init__(self, game, index):
        super().__init__(game)
        self.player = game.get_player(index)
        self.auction = AuctionLogic(self)

    def run(self, text):
        self.game.console.run(text)

    def play(self):
        while self.game.console.turn_mgr.can_roll:
            if self.game.console.auction_running():
                self.auction.auction(self.game.console.get_current_tile())
            elif self.game.console.trade_loaded():
                self.run("accept")
                return
            else:
                self.run("roll")
                tile = self.game.console.get_current_tile()
                try:
                    if self.player.has(tile.price):
                        self.run("buy")
                    else:
                        self.run("auction")
                except AttributeError:
                    pass
        self.run("next")
