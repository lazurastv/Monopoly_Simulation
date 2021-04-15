import random as rand
import numpy as np

tile_count = 4
max_die = 3
throws = 100000

start = 0
tile = start
occurrences = np.zeros(tile_count)
rounds = 0

for i in range(throws):
    die_1 = rand.randint(1, max_die)
    die_2 = rand.randint(1, max_die)
    tile += die_1 + die_2
    if tile >= tile_count:
        rounds += 1
        tile %= tile_count
    if tile == 1 and rand.random() < 0.5:
        tile = 3
    occurrences[tile] += 1


# occurrences /= rounds
# occurrences /= throws
print(occurrences)
print([1/4, 1/7, 1/4, 5/14])

"""
0: [0.      0.1656  0.33604 0.49836]
1: [0.3327  0.      0.33353 0.33377]
2: [0.33403 0.16522 0.      0.50075]
3: [0.32976 0.1683  0.33617 0.16577]

no repeats: [0.250008 0.117303 0.250084 0.382605]
repeats: [0.249921 0.117438 0.249957 0.382684]
"""
