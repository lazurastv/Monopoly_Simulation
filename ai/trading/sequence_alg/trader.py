from copy import deepcopy


class Trader:
    def __init__(self, groups, player_count):
        self.groups = groups
        self.player_count = player_count
        self.nodes = []
        self.positions = []

    def solve_for(self, player):
        self.get_valid_positions([player], self.groups, {})

    def get_valid_positions(self, players, groups, nodes, index=0):
        if len(players) == self.player_count:
            return
        target = players[index]
        for group in groups:
            groups_copy = groups.copy()
            groups_copy.remove(group)
            players_copy = players.copy()
            nodes_copy = nodes.copy()
            for tile, player in group:
                if player != target:
                    if target not in nodes_copy:
                        nodes_copy[target] = {player: [tile]}
                    elif player not in nodes_copy[target]:
                        nodes_copy[target][player] = [tile]
                    else:
                        nodes_copy[target][player].append(tile)
                    if player not in players_copy:
                        players_copy.append(player)
            if index + 1 == len(players_copy):
                self.nodes.append(nodes_copy)
            else:
                self.get_valid_positions(players_copy, groups_copy, nodes_copy, index + 1)

    def walk(self, source, dest, nodes, next_graph):
        nodes_copy = deepcopy(nodes)
        current_node = nodes_copy.pop(source)
        for node in current_node:
            if node in nodes_copy:
                next_graph_copy = deepcopy(next_graph)
                if len(next_graph_copy[source]) > 1:
                    next_graph_copy[source].pop(node)
                else:
                    next_graph_copy.pop(source)
                if node == dest:
                    self.positions.append([source, current_node[node], next_graph_copy])
                else:
                    self.walk(node, dest, nodes_copy, next_graph_copy)

    def consider_position(self, position, player):
        bars = []
        for bar in position[player]:
            bars.append(bar)
        positions = [0, 0, position]
        while len(bars) > 0:
            bar = bars.pop()
            for _, _, pos in positions:
                self.walk(bar, player, pos, pos)
                for posit in self.positions:
                    last_node = posit[0]
                    tiles = position[last_node][player]
                    try:
                        posit[2][bar][last_node].append(*tiles)
                    except KeyError:
                        posit[2][bar][last_node] = tiles


example = [[(0, 0), (1, 0), (2, 2)], [(3, 1), (4, 1), (5, 2)], [(6, 0), (7, 1), (8, 2)], [(9, 0), (10, 1), (11, 0)]]
solver = Trader(example, 4)
solver.solve_for(0)
solution = solver.nodes[0]
print(solution)
solver.walk(0, 1, solution, solution.copy())
print(solver.positions)

"""

    def find_trade(self, source, visited, groups, trades):
        if len(visited) == self.player_count:
            return
        for group in groups:
            groups_copy = groups.copy()
            groups_copy.remove(group)
            trades_copy = trades.copy()
            for tile, player in group:
                if source == self.start and player != self.start:
                    try:
                        trades_copy[player].insert(tile, 0)
                    except KeyError:
                        trades_copy[player] = [tile, "<->"]
                elif source != self.start and player == self.start:
                    trades_copy.append(tile)
                elif player != source:
                    visited_copy = visited.copy()
                    visited_copy.append(player)
                    self.find_trade(player, visited_copy, groups_copy, trades_copy[player])
            if isinstance(trades_copy, dict):
                for player in trades_copy:
                    visited_copy = visited.copy()
                    visited_copy.append(player)
                    self.find_trade(player, visited_copy, groups_copy, trades_copy[player])
                if trades_copy[source][-1] != "<->":
                    self.trades.append(trades_copy)

"""