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


def type_input(target_type):
    value = input()
    while not (value := is_type(value, target_type)):
        print("Incorrect type! Must be", target_type.__name__)
        value = input()
    return value


def is_type(value, target_type):
    try:
        return target_type(value)
    except ValueError:
        return None


def throw_dice():
    return randint(1, 6), randint(1, 6)