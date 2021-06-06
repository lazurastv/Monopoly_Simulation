from ai.trading.walker import Walker


def add_graphs(next_graphs, source):
    for next_graph in source:
        if next_graph not in next_graphs:
            next_graphs.append(next_graph)


class TradeConstructor:
    def __init__(self, player):
        self.player = player

    def construct_all_bars(self, graph):
        bars = graph.get_node(self.player)
        graphs = [graph]
        all_trades = {}
        for bar in bars:
            next_graphs, trades = self.construct_all_graphs(graphs, bar)
            if trades is None:
                return
            all_trades[bar] = trades
            graphs = next_graphs
        return all_trades

    def construct_all_graphs(self, graphs, bar):
        next_graphs = []
        trades = None
        for graph in graphs:
            walker = self.construct_graph(graph, bar)
            if walker.trades_found():
                add_graphs(next_graphs, walker.final_graphs)
                trades = walker.trades
        return next_graphs, trades

    def construct_graph(self, graph, bar):
        walker = Walker(graph)
        walker.find_trades(self.player, bar)
        return walker
