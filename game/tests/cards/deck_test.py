import unittest
import numpy

from game.cards.deck import Deck


class PlayerTest(unittest.TestCase):
    def test_init_community(self):
        deck = Deck("Community")
        self.assertEqual(16, len(deck.cards))

    def test_init_chance(self):
        deck = Deck("Chance")
        self.assertEqual(16, len(deck.cards))

    def test_shuffle(self):
        deck = Deck("Community")
        deck.cards = list(range(10))
        prob = numpy.zeros((10, 10))
        expected_mean = 4.5
        expected_variance = 8.25
        for i in range(1000):
            deck.shuffle()
            for pos, number in enumerate(deck.cards):
                prob[pos, number] += 1
        for i in range(10):
            for j in range(10):
                prob[i, j] /= 1000
        for i in range(10):
            mean = 0
            variance = 0
            for j in range(10):
                mean += prob[i, j] * j
                variance += prob[i, j] * (4.5 - j) ** 2
            self.assertAlmostEqual(expected_mean, mean, delta=0.4)
            self.assertAlmostEqual(expected_variance, variance, delta=0.8)


if __name__ == '__main__':
    unittest.main()
