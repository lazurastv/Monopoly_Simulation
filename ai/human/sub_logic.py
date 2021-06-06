class SubLogic:
    def __init__(self, logic):
        self.logic = logic

    def run(self, text):
        self.logic.run(text)

    def get_player(self):
        return self.logic.player

    def get_properties(self):
        return self.get_player().properties

    def get_current_tile(self):
        return self.logic.game.console.get_current_tile()