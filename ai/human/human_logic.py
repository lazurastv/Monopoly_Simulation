from ai.human.trading_logic import TradingLogic


class HumanLogic:
    def __init__(self, game, index):
        self.console = game.console
        self.game = game
        self.player = game.get_player(index)
        self.trading = TradingLogic()

    def trade(self):
        self.trading

    def perform_turn(self):
        self.trade()
        self.console.run("roll")
        self.console.turn_mgr.get_current_tile()
