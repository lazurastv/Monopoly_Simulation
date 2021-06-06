from ai.trading.sequence_alg.combiner import Combiner
from ai.trading.sequence_alg.trade_constructor import TradeConstructor


class Trader:
    def __init__(self, target, groups, player_count):
        self.target = target
        self.groups = groups
        self.player_count = player_count

    def solve_for(self):
        combiner = Combiner(self.player_count, self.groups)
        combiner.combine_with(self.target)
        trade_const = TradeConstructor(self.target)
        for graph in combiner:
            trade = trade_const.construct_all_bars(graph)
            if trade is not None:
                return trade


def encode_group(text):
    text = text.split()
    encoded_group = []
    i = 0
    for group in text:
        group_list = []
        for char in group:
            group_list.append((i, int(char)))
            i += 1
        encoded_group.append(group_list)
    return encoded_group


if __name__ == "__main__":
    example = encode_group("002 112 324 304 304")
    solver = Trader(0, example, 5)
    trades = solver.solve_for()
    print(trades)
