class Node:
    def __init__(self, index):
        self.index = index
        self.pointers = {}
        self.visited = False

    def __iter__(self):
        return iter(self.pointers)

    def __str__(self):
        return str(self.pointers)

    def __repr__(self):
        return self.__str__()

    def add_pointer(self, pointer_index, *value):
        if self.index == pointer_index:
            return
        if pointer_index not in self.pointers:
            self.pointers[pointer_index] = []
        for val in value:
            if val not in self.pointers[pointer_index]:
                self.pointers[pointer_index].append(val)

    def redirect_pointer(self, pointer_index, new_pointer_index):
        tiles = self.pop(pointer_index)
        self.add_pointer(new_pointer_index, *tiles)

    def pop(self, pointer):
        return self.pointers.pop(pointer)

    def get_pointer(self, pointer):
        return self.pointers[pointer]

    def pointer_count(self):
        return len(self.pointers)
