from random import randint


class Dice:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.repeats = 0

    def __str__(self):
        return str(self.first) + ", " + str(self.second) + ", roll " + str(self.repeats + 1)

    def roll(self):
        self.first = randint(1, 6)
        self.second = randint(1, 6)
        if self.same():
            self.repeats += 1

    def same(self):
        return self.first == self.second

    def value(self):
        return self.first + self.second
