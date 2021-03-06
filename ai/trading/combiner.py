from copy import deepcopy
from ai.trading.graph import Graph


def complete_group_with(group, target, valid_solution, partners):
    for tile, player in group:
        valid_solution.add_pointer(target, player, tile)
        if player not in partners:
            partners.append(player)


def has_next(index, partners):
    return len(partners) > index + 1


class Combiner:
    def __init__(self, groups):
        self.groups = groups
        self.graphs = []

    def __iter__(self):
        return iter(self.graphs)

    def __str__(self):
        return str(self.graphs)

    def combine_with(self, target):
        self.complete_all_groups([target], self.groups, Graph())
        self.graphs.sort(key=len)
        return self.graphs

    def complete_all_groups(self, partners, groups, graph, index=0):
        target = partners[index]
        for group in groups:
            graph_copy = deepcopy(graph)
            partners_copy = deepcopy(partners)
            complete_group_with(group, target, graph_copy, partners_copy)
            if has_next(index, partners_copy):
                groups_copy = deepcopy(groups)
                groups_copy.remove(group)
                self.complete_all_groups(partners_copy, groups_copy, graph_copy, index + 1)
            else:
                redundant_graph = False
                for good_graph in self.graphs:
                    if good_graph.equivalent(graph_copy):
                        redundant_graph = True
                if not redundant_graph:
                    self.graphs.append(graph_copy)
