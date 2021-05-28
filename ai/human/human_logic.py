from ai.human.logic import Logic


class HumanLogic(Logic):
    def __init__(self, game, index):
        super().__init__(game)
        self.player = game.get_player(index)

    def run(self, text):
        self.game.console.run(text)

    def play(self):
        for i in range(3):
            if self.game.console.auction_running():
                val = self.game.console.auction.value + 1
                if self.player.has(val):
                    self.run("bet " + str(val))
                else:
                    self.run("end")
                return
            elif self.game.console.trade_loaded():
                self.run("accept")
                return
            else:
                self.run("roll")
                self.run("buy")
                self.run("auction")
        self.run("next")
