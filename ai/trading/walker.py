from copy import deepcopy


class Walker:
    def __init__(self, graph):
        self.graph = graph
        self.start = -1
        self.end = -1
        self.exclude = -1
        self.final_graphs = []
        self.trades = []

    def find_trades(self, player, bar):
        self.find_route(bar, player)
        trades = deepcopy(self.trades)
        graphs = deepcopy(self.final_graphs)
        self.find_route(player, player, bar)
        for trade in self.trades:
            try:
                trades.remove(trade)
            except (KeyError, ValueError):
                continue
        self.trades = []
        for source, trade in trades:
            self.trades.append(trade)
            for graph in graphs:
                graph.pop(player, bar)
                graph.redirect_pointer(source, player, bar)
        self.trades.append("<->")
        self.trades.append(self.graph.get_pointer(player, bar))
        self.final_graphs = graphs

    def trades_found(self):
        return self.trades[0] != "<->"

    def find_route(self, start, end, without=-1):
        self.start = start
        self.end = end
        self.exclude = without
        self.final_graphs = []
        self.trades = []
        self.graph.reset()
        self.walk(start, self.graph)

    def add_solution(self, source, graph):
        current_tiles = graph.get_pointer(source, self.end)
        trade = (source, current_tiles)
        if graph not in self.final_graphs:
            self.final_graphs.append(graph)
        if trade not in self.trades:
            self.trades.append(trade)

    def walk(self, source, graph):
        current_node = graph.go_to_node(source)
        for pointer in current_node:
            if pointer != self.exclude:
                if pointer == self.end:
                    self.add_solution(source, graph)
                elif not graph.visited(pointer):
                    graph_copy = deepcopy(graph)
                    graph_copy.pop(source, pointer)
                    self.walk(pointer, graph_copy)
