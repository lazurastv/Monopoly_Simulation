from ai.trading.tree_alg.node import Node


class Branch(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def __str__(self):
        val = ""
        for node in self.children:
            val += str(node) + ", "
        return val
