class Trader:
    def __init__(self, groups, player_count):
        self.groups = groups
        self.player_count = player_count
        self.bars = []

    def solve_for(self, player):
        self.complete_group([player], self.groups, {})

    def complete_group(self, players, groups, bars, index=0):
        if len(players) == self.player_count:
            return
        target = players[index]
        for group in groups:
            groups_copy = groups.copy()
            groups_copy.remove(group)
            players_copy = players.copy()
            bars_copy = bars.copy()
            for tile, player in group:
                if player != target:
                    if target not in bars_copy:
                        bars_copy[target] = {player: [tile]}
                    elif player not in bars_copy[target]:
                        bars_copy[target][player] = [tile]
                    else:
                        bars_copy[target][player].append(tile)
                    if player not in players_copy:
                        players_copy.append(player)
            if index + 1 == len(players_copy):
                self.bars.append(bars_copy)
            else:
                self.complete_group(players_copy, groups_copy, bars_copy, index + 1)

    def construct_solution(self, players, bars):
        for player in players:
            exclusions = []
            failed = False
            sol = None
            for problem in bars[player]:
                sol = self.move(player, problem, bars, [], exclusions)
                if sol is None:
                    failed = True
                    break
                exclusions.append(problem)
            if not failed:
                return sol

    def move(self, start, end, bars, sequence, exclude=None):
        bars_copy = bars.copy()
        start_problems = bars_copy.pop(start)
        for node in bars_copy:
            if start in bars_copy[node] and node not in start_problems:
                sequence_copy = sequence.copy()
                sequence_copy.append(bars_copy[node][start])
                if node == end and (exclude is None or node not in exclude):
                    # sequence_copy.append()
                    return sequence_copy
                else:
                    return self.move(node, end, bars_copy, sequence_copy, exclude)


example = [[(0, 0), (1, 0), (2, 2)], [(3, 1), (4, 1), (5, 2)], [(6, 0), (7, 1), (8, 2)], [(9, 0), (10, 1), (11, 0)]]
solver = Trader(example, 4)
solver.solve_for(0)
solution = solver.bars[0]
print(solution)
print(solver.construct_solution([0, 1, 2], solution))
