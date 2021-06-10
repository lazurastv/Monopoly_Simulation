from ai.logic.logic import Logic


class ManualLogic(Logic):
    def play(self):
        try:
            self.game.console.run(input())
        except Exception as e:
            print(e)
