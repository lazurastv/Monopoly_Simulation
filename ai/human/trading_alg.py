from ai.human.matrix import Matrix


def clean_groups(groups):
    cleaned_groups = []
    to_remove = []
    for group in groups:
        owner = group[0][1]
        multiple_owners = False
        useful = True
        for tile, player in group:
            if player != owner:
                multiple_owners = True
            elif player is None:
                useful = False
        if useful:
            if multiple_owners:
                cleaned_groups.append(group)
            else:
                to_remove.append(group)
    for group in to_remove:
        groups.remove(group)
    return cleaned_groups


class TradeFinder:
    def __init__(self, player_count, groups):
        self.player_count = player_count
        self.groups = groups
        self.solution = None
        self.lowest_player_count = 0

    def solve_for(self, player):
        groups = clean_groups(self.groups)
        solution = Matrix(self.player_count)
        self.lowest_player_count = self.player_count
        self.complete_group([player], groups, solution)

    def check_solution(self, solution, players):
        # command_stream = []
        max_player = max(players)
        for i in players:
            for j in players:
                if j >= i:
                    break
                tiles_a = solution.get(i, j)
                tiles_b = solution.get(j, i)
                if len(tiles_a) > 0 or len(tiles_b) > 0:
                    groups = self.groups.copy()
                    for tile in tiles_a:
                        for group in groups:
                            if (tile, j) in group:
                                group.remove((tile, j))
                                group.append((tile, i))
                                break
                    for tile in tiles_b:
                        for group in groups:
                            if (tile, i) in group:
                                group.remove((tile, i))
                                group.append((tile, j))
                                break
                    groups = clean_groups(groups)
                    new_finder = TradeFinder(self.player_count, groups)
                    for k in players:
                        check = False
                        for l in range(max_player):
                            if len(solution.get(l, k)) != 0:
                                check = True
                                break
                        if check:
                            new_finder.solve_for(k)
                            if not new_finder.solution.__eq__(solution):
                                return False
                        solution.remove(i, j)
                        solution.remove(j, i)
                        if solution.empty():
                            return True
                        else:
                            return self.check_solution(solution, players)

    def complete_group(self, players, groups, solution, index=0):
        if len(players) >= self.lowest_player_count:
            return
        target = players[index]
        for group in groups:
            groups_copy = groups.copy()
            groups_copy.remove(group)
            players_copy = players.copy()
            solution_copy = solution.__deepcopy__()
            for tile, player in group:
                if player != target:
                    solution_copy.append(target, player, tile)
                    if player not in players_copy:
                        players_copy.append(player)
            player_count = len(players_copy)
            if index + 1 < player_count:
                self.complete_group(players_copy, groups_copy, solution_copy, index + 1)
            elif self.lowest_player_count > player_count:
                if self.check_solution(solution_copy.__deepcopy__(), players_copy):
                    self.lowest_player_count = len(players)
                    self.solution = solution_copy
