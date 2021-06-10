from ai.trading.node import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return str(self.nodes)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, item):
        return item in self.nodes

    def __iter__(self):
        return iter(self.nodes)

    def add_pointer(self, node_index, pointer_index, pointer_value):
        if node_index not in self:
            self.nodes[node_index] = Node(node_index)
        self.nodes[node_index].add_pointer(pointer_index, pointer_value)

    def redirect_pointer(self, node_index, pointer_index, new_pointer_index):
        self.nodes[node_index].redirect_pointer(pointer_index, new_pointer_index)

    def pop(self, node_index, pointer_index):
        try:
            self.nodes[node_index].pop(pointer_index)
            return
        except KeyError:
            pass
        try:
            if self.nodes[node_index].pointer_count() == 0:
                self.nodes.pop(node_index)
        except KeyError:
            return

    def go_to_node(self, node):
        node = self.nodes[node]
        node.visited = True
        return node

    def get_node(self, node_index):
        return self.nodes[node_index]

    def get_pointer(self, node_index, pointer_index):
        return self.nodes[node_index].get_pointer(pointer_index)

    def reset(self):
        for node in self:
            self.nodes[node].visited = False

    def visited(self, node):
        return self.nodes[node].visited

    def equivalent(self, graph):
        for player in graph:
            if player not in self:
                return False
        return True

    def unroll(self):
        tile_list = []
        for node_index in self:
            node = self.get_node(node_index)
            for bar in node:
                tiles = node.get_pointer(bar)
                for tile in tiles:
                    tile_list.append((bar, tile))
        return tile_list
