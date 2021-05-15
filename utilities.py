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


def force_type_input(target_type):
    while True:
        try:
            return target_type(input())
        except ValueError:
            print("Incorrect type! Must be", target_type.__name__)


def throw_dice():
    return randint(1, 6), randint(1, 6)