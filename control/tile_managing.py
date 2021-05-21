def buy(tile, player):
    try:
        tile.buy(player)
    except AttributeError:
        print("Tile is not a property!")


def buy_house(tile, player):
    try:
        tile.buy_house(player)
    except AttributeError:
        print("Tile is not an improvable tile!")


def sell_house(tile, player):
    try:
        tile.sell_house(player)
    except AttributeError:
        print("Tile is not an improvable tile!")


def mortgage(tile, player):
    try:
        tile.take_mortgage(player)
    except AttributeError:
        print("Tile is not a property!")


def repay(tile, player):
    try:
        tile.pay_mortgage(player)
    except AttributeError:
        print("Tile is not a property!")
