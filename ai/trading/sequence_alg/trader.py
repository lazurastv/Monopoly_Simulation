from copy import deepcopy


def remove_connection(next_graph_copy, source, node):
    if len(next_graph_copy[source]) > 1:
        next_graph_copy[source].pop(node)
    else:
        next_graph_copy.pop(source)


def inherit(graph, target, giver, gift):
    tiles = graph[gift].pop(giver)
    if target == gift:
        return
    try:
        for tile in tiles:
            graph[gift][target].append(tile)
    except KeyError:
        try:
            graph[gift][target] = tiles
        except KeyError:
            graph[gift] = {target: tiles}


class Trader:
    def __init__(self, groups, player_count):
        self.groups = groups
        self.player_count = player_count
        self.valid_solutions = []
        self.graphs = []
        self.trades = []

    def solve_for(self, target):
        self.get_valid_solutions([target], self.groups, {})
        self.valid_solutions.sort(key=len)
        for graph in self.valid_solutions:
            constructed_solution = self.construct_solution(graph, target)
            if constructed_solution is not None:
                for player in constructed_solution:
                    if self.construct_solution(graph, player) is None:
                        return None
                return constructed_solution

    def get_valid_solutions(self, players, groups, valid_solution, index=0):
        if len(players) >= self.player_count:
            return
        target = players[index]
        for group in groups:
            groups_copy = groups.copy()
            groups_copy.remove(group)
            players_copy = players.copy()
            valid_solution_copy = valid_solution.copy()
            for tile, player in group:
                if player != target:
                    if target not in valid_solution_copy:
                        valid_solution_copy[target] = {player: [tile]}
                    elif player not in valid_solution_copy[target]:
                        valid_solution_copy[target][player] = [tile]
                    else:
                        valid_solution_copy[target][player].append(tile)
                    if player not in players_copy:
                        players_copy.append(player)
            if index + 1 == len(players_copy):
                self.valid_solutions.append(valid_solution_copy)
            else:
                self.get_valid_solutions(players_copy, groups_copy, valid_solution_copy, index + 1)

    def add_solution(self, source, node, final_graph_copy):
        current_tiles = final_graph_copy[source][node].copy()
        if final_graph_copy not in self.graphs:
            self.graphs.append(final_graph_copy)
        if (source, current_tiles) not in self.trades:
            self.trades.append((source, current_tiles))

    def walk(self, start, source, dest, graph, final_graph, exclude=-1):
        graph_copy = deepcopy(graph)
        current_node = graph_copy.pop(source)
        for node in current_node:
            final_graph_copy = deepcopy(final_graph)
            if node != exclude and (node in graph_copy or node == dest):
                if node == dest:
                    self.add_solution(source, node, final_graph_copy)
                else:
                    remove_connection(final_graph_copy, source, node)
                    self.walk(start, node, dest, graph_copy, final_graph_copy, exclude)

    def construct_solution(self, true_graph, player):
        graph = deepcopy(true_graph)
        bars = graph.pop(player)
        graphs = [graph]
        trades = {}
        for bar in bars:
            trades[bar] = [bars[bar]]
            self.trades = []
            self.graphs = []
            for pos in graphs:
                self.walk(bar, bar, player, pos, pos)
                for source, tiles in self.trades:
                    trades[bar].append(tiles)
                self.trades = []
                for not_bar in bars:
                    if bar != not_bar:
                        self.walk(not_bar, not_bar, player, pos, pos, bar)
                for source, tiles in self.trades:
                    if tiles in trades[bar]:
                        trades[bar].remove(tiles)
                for source, tiles in self.trades:
                    inherit(pos, bar, player, source)
            graphs = deepcopy(self.graphs)
            if len(graphs) == 0:
                return None
        return trades


example = [[(0, 0), (1, 0), (2, 2)],
           [(3, 1), (4, 1), (5, 2)],
           [(6, 3), (7, 2), (8, 4)],
           [(9, 3), (10, 0), (11, 4)],
           [(12, 3), (13, 0), (14, 4)]]
solver = Trader(example, 5)
print(solver.solve_for(3))
