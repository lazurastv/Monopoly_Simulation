from ai.human.leverage import Leverage


class StrongLeverage(Leverage):
    def __init__(self, player_count):
        super().__init__(player_count)

    def update(self):
        for group in self.groups