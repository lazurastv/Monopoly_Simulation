from ai.trading.combiner import Combiner
from ai.trading.trade_constructor import TradeConstructor


def solve_for(target, groups, player_count):
    combiner = Combiner(groups, player_count)
    combiner.combine_with(target)
    trade_const = TradeConstructor(target)
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
    example = encode_group("002 112 012 010")
    trades = solve_for(1, example, 4)
    print(trades)
