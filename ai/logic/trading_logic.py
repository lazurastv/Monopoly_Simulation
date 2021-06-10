from ai.logic.sub_logic import SubLogic
from ai.trading.communicator import Communicator
from ai.trading.money_calculator import MoneyCalculator


class TradingLogic(SubLogic):
    def __init__(self, logic):
        super().__init__(logic)
        money_calc = MoneyCalculator(logic)
        self.communicator = Communicator(logic.player.id, logic.game, money_calc)

    def trade(self):
        commands = self.communicator.get_trade()
        if commands is None:
            return
        for command in commands:
            self.run(command)
