class Leverage:
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append([])
            for j in range(size):
                self.data[i].append(set())
        self.size = size

    def add(self, group, i, j):
        if i > j:
            tmp = i
            i = j
            j = tmp
        self.data[i][j].add(group)

    def add_many(self, group, *indexes):
        size = len(indexes)
        for i in range(size):
            for j in range(i + 1, size):
                self.add(group, indexes[i], indexes[j])

    def get(self, i, j):
        if i > j:
            return self.data[j][i]
        else:
            return self.data[i][j]
