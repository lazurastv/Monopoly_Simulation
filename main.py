# players =
# shuffle(players)
# shuffle(community_chest)
# shuffle(treasure)

def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def show(text):
    print(text)


def stat():
    print("Text")


keywords = {
    "add": (add, int, int),
    "sub": (sub, int, int),
    "show": (show, str),
    "stat": (stat,)
}


from Console import Console


cn = Console(keywords, 3)

while True:
    cn.parse_text(input())


"""
def fun():
    print("Input a number:", end=" ")
    try:
        print(int(input()))
        return False
    except ValueError:
        print("Input must be an integer!")
        return True


while fun():
    pass


while True:
    print("Input a number:", end=" ")
    try:
        print(int(input()))
        break
    except ValueError:
        print("Input must be an integer!")
"""