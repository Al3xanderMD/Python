class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.data = [[0] * m for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            raise IndexError("Index out of range")

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value
        else:
            raise IndexError("Index out of range")

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(i, j)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

if __name__ == "__main__":
    matrix = Matrix(2, 3)
    for i in range(2):
        for j in range(3):
            matrix.set(i, j, i * 3 + j)

    print("Original Matrix:")
    print(matrix)

    transposed = matrix.transpose()
    print("Transposed Matrix:")
    print(transposed)

    identity = Matrix(3, 3)
    identity.apply(lambda i,j:1 if i == j else 0)
    print("Identity Matrix:")
    print(identity)

    result = matrix * transposed
    print("Matrix Multiplication Result:")
    print(result)
