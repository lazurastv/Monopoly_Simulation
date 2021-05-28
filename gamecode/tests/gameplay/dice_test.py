import unittest

from gamecode.gameplay.dice import Dice


class MyTestCase(unittest.TestCase):
    def test_one_distribution(self):
        dice = Dice()
        prob = [0] * 6
        expected_mean = 3.5
        expected_variance = 17.5 / 6
        for _ in range(1000):
            dice.throw()
            prob[dice.first - 1] += 1
        for i in range(6):
            prob[i] /= 1000
        mean = 0
        variance = 0
        for i in range(6):
            mean += prob[i] * (i + 1)
            variance += prob[i] * (i + 1 - expected_mean) ** 2
        self.assertAlmostEqual(mean, expected_mean, delta=0.3, msg=mean)
        self.assertAlmostEqual(variance, expected_variance, delta=0.2, msg=variance)

    def test_total_distribution(self):
        dice = Dice()
        prob = [0] * 11
        expected_mean = 7
        expected_variance = 35 / 6
        for _ in range(1000):
            dice.throw()
            prob[dice.value() - 2] += 1
        for i in range(11):
            prob[i] /= 1000
        mean = 0
        variance = 0
        for i in range(11):
            mean += prob[i] * (i + 2)
            variance += prob[i] * (i + 2 - expected_mean) ** 2
        self.assertAlmostEqual(mean, expected_mean, delta=0.7, msg=mean)
        self.assertAlmostEqual(variance, expected_variance, delta=0.6, msg=variance)

    def test_repeats_distribution(self):
        dice = Dice()
        expected_mean = 1 / 6
        expected_variance = 5 / 36
        for _ in range(1000):
            dice.throw()
        mean = dice.repeats / 1000
        variance = (24 * mean + 1) / 36
        self.assertAlmostEqual(mean, expected_mean, delta=0.1, msg=mean)
        self.assertAlmostEqual(variance, expected_variance, delta=0.1, msg=variance)


if __name__ == '__main__':
    unittest.main()
