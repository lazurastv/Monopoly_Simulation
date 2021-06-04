from ai.trading.tree_alg.branch import Branch
from ai.trading.tree_alg.node import Node


class Trader:
    def __init__(self, players, groups):
        self.trees = {}
        self.init_trees(players, groups)

    def init_trees(self, players, groups):
        for player in players:
            self.trees[player] = Node(player)
        for i, player in enumerate(players):
            tile_name = 'a'
            target_tree = self.trees[i]
            for j, group in enumerate(groups):
                branch = Branch(j)
                for owner in group:
                    if owner != player:
                        node = Node((tile_name, self.trees[owner]))
                        branch.add(node)
                    tile_name = chr(ord(tile_name) + 1)
                target_tree.add(branch)

    def solve_for(self, target):
        pass


task = [(0, 0, 2), (1, 1, 2), (0, 1, 2), (0, 1, 0)]
tt = Trader(list(range(3)), task)
print(tt.trees[0].get(1, 1))
tt.solve_for(0)
