from ai.logic.logic import Logic


class ManualLogic(Logic):
    def play(self):
        self.game.console.run(input())
