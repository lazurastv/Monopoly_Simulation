class SubLogic:
    def __init__(self, logic):
        self.logic = logic

    def run(self, text):
        self.logic.run(text)

    def get_player(self):
        return self.logic.player
