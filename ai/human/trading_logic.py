from ai.human.leverage import Leverage


class TradingLogic:
    def __init__(self, logic):
        self.logic = logic
        n = self.logic.game.get_player_count()
        self.groups = self.logic.game.get_groups()
        to_remove = []
        for group in self.groups:
            if group.name == "utility" or group.name == "railroad":
                to_remove.append(group)
        for group in to_remove:
            self.groups.remove(group)
        self.strong_leverage = Leverage(n)
        self.weak_leverage = Leverage(n)

    def analyze_leverages(self):
        to_remove = []
        for group in self.groups:
            if not group.filled():
                continue
            owners = group.owners()
            n = len(owners)
            if n == 1:
                to_remove.append(group)
            elif n == 2:
                id_1 = owners[0].index
                id_2 = owners[1].index
                self.strong_leverage.add(group, id_1, id_2)
            else:
                id_1 = owners[0].index
                id_2 = owners[1].index
                id_3 = owners[2].index
                self.weak_leverage.add_many(group, id_1, id_2, id_3)
        for group in to_remove:
            self.groups.remove(group)


# registry of strong and weak leverage
# 0,2 - 2 leverage is an instant exchange (with money aiming to equalize their income and development
# 0,2,3 and 1,2,3 can translate to 0,2,2 and 1,3,3, so 0,2 and 1,3 strong leverage
# money calculation: we trade a group which makes 150 at start for a group with 400 at start.
# we trade enough money to build house to equalize this income. Note that growth is also different, so
# we must account for different growth. 150 to 225, while 450 to 600 is both one house each, but more difference.
# Assuming each tile is equally likely, we should also give the difference to the worse side to account
# for the loss. This difference should be given as many times, as the tiles are visited on average per game.
