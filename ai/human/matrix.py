class Matrix:
    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                self.matrix[i].append([])

    def __eq__(self, other):
        return self.matrix.__eq__(other.matrix)

    def get(self, i, j):
        return self.matrix[i][j]

    def remove(self, i, j):
        self.matrix[i][j] = []

    def append(self, i, j, val):
        self.matrix[i][j].append(val)

    def empty(self):
        size = 0
        for row in self.matrix:
            for column in row:
                size += len(column)
        return size == 0

    def __deepcopy__(self):
        matrix_copy = Matrix(len(self.matrix))
        matrix = []
        for row in self.matrix:
            row_copy = []
            for column in row:
                row_copy.append(column.copy())
            matrix.append(row_copy)
        matrix_copy.matrix = matrix
        return matrix_copy
