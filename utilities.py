from random import randint


def shuffle(array):
    n = len(array)
    for i in range(0, n):
        j = randint(0, n - 1)
        while i == j:
            j = randint(0, n - 1)
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp