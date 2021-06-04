class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def add(self, node):
        self.children.append(node)

    def set(self, value):
        self.value = value

    def get(self, branch_index, node_index=None):
        branch = self.children[branch_index]
        if node_index is None:
            return branch
        else:
            return branch.get(node_index)
