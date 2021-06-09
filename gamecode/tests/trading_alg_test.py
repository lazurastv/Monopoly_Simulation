import unittest
from random import randint, seed

from ai.logic.trading_alg import TradeFinder, clean_groups


def random_group(player_count, group_count):
    group = []
    seed()
    for i in range(group_count):
        group_i = []
        for j in range(3):
            group_i.append([i * 3 + j, randint(0, player_count - 1)])
        group.append(group_i)
    return group


class MyTestCase(unittest.TestCase):
    def test_specific(self):
        player_count = 5
        groups = [[(0, 0), (1, 0), (2, 2)],
                  [(3, 1), (4, 1), (5, 2)],
                  [(6, 3), (7, 2), (8, 4)],
                  [(9, 3), (10, 0), (11, 4)],
                  [(12, 3), (13, 0), (14, 4)]]
        # random_group(player_count, 8)
        finder = TradeFinder(player_count, groups)
        for group in clean_groups(finder.groups):
            print(group)
        finder.solve_for(0)
        if finder.solution is None:
            print("No solution found!")
        else:
            print("Solution")
            for row in finder.solution.matrix:
                print(row)

    def test_random_players(self):
        player_count = 4
        groups = random_group(player_count, 8)
        finder = TradeFinder(player_count, groups)
        for group in clean_groups(finder.groups):
            print(group)
        finder.solve_for(0)
        if finder.solution is None:
            print("No solution found!")
        else:
            print("Solution")
            for row in finder.solution.matrix:
                print(row)


if __name__ == '__main__':
    unittest.main()

""""[[(0, 1), (1, 1), (2, 3)],
[(3, 0), (4, 1), (5, 2)],
[(6, 3), (7, 0), (8, 0)],
[(9, 2), (10, 3), (11, 2)],
[(12, 2), (13, 1), (14, 2)],
[(15, 1), (16, 1), (17, 3)],
[(18, 2), (19, 0), (20, 0)],
[(21, 2), (22, 0), (23, 0)]]"""
