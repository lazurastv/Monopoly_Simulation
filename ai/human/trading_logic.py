from ai.human.sub_logic import SubLogic
from ai.trading.communicator import Communicator


class TradingLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)
        self.logic = logic
        self.communicator = Communicator(logic.player.id, logic.game)

    def trade(self):
        commands = self.communicator.get_trade()
        if commands is None:
            return
        for command in commands:
            self.run(command)
