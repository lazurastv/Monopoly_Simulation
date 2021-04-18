from random import randint


def shuffle(array):
    n = len(array)
    for i in range(0, n):
        j = randint(0, n)
        while i == j:
            j = randint(0, n)
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
    return array


end_game = False

players = range(1, 10)
new_players = shuffle(players)

while not end_game:
    print(players, new_players)
    end_game = True
