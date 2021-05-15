from abc import abstractmethod


class Tile:

    def __init__(self, name, index):
        self.name = name
        self.index = index

    @abstractmethod
    def event(self, player):
        pass
