from random import randint


class Dice:
    def __init__(self):
        self.value = 0
        self.repeats = 0

    def throw(self):
        first = randint(1, 6)
        second = randint(1, 6)
        if first == second:
            self.repeats += 1
        self.value = first + second
        return self.value
