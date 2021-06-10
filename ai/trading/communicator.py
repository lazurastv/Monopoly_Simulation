from ai.trading.trader import solve_for


def get_groups(groups):
    int_groups = []
    for group in groups:
        if not group.filled():
            continue
        next_group = []
        for tile in group:
            next_group.append((tile.position, tile.owner.id))
        int_groups.append(next_group)
    return int_groups


def clean_groups(groups):
    remove = []
    for group in groups:
        if group.owned():
            remove.append(group)
    for group in remove:
        groups.remove(group)


class Communicator:
    def __init__(self, target, game, money_calc):
        self.target = target
        self.game = game
        self.money_calc = money_calc
        self.groups = game.get_groups(True)

    def get_trade(self):
        clean_groups(self.groups)
        int_groups = get_groups(self.groups)
        trades, prices = solve_for(self.target, int_groups, self.money_calc)
        if trades is None:
            return None
        commands = []
        for bar, trade in trades:
            command = "trade " + str(bar) + " " + str(prices[self.target][bar])
            for tiles in trade:
                if tiles != "<->":
                    for tile in tiles:
                        command += " " + str(tile)
            commands.append(command)
        return commands
