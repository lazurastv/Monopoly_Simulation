from ai.trading.combiner import Combiner
from ai.trading.trade_constructor import TradeConstructor


def solve_for(target, groups, money_calc):
    combiner = Combiner(groups)
    combiner.combine_with(target)
    money_calc.calculate_prices(combiner.graphs)
    trade_const = TradeConstructor(target)
    for i, graph in enumerate(combiner):
        trade = trade_const.construct_all_bars(graph)
        if trade is not None and money_calc.verify_trades(i, trade):
            return trade, money_calc.get(i)
    return None, None


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
