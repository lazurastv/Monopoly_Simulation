from random import randint


class Deck:
    def __init__(self):
        self.cards = []
        self.next = 0

    def shuffle(self):
        n = len(self.cards)
        for i in range(n):
            j = randint(0, n - 1)
            # while i == j: - is this needed?
            #     j = randint(0, n - 1)
            tmp = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = tmp

    def draw(self):
        card = self.cards[self.next].copy()
        self.next += 1
        self.next %= len(self.cards)
        return card
