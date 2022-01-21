class Matrix:

    def __init__(self, data):

        self.data = data
        self.row = len(self.data)
        self.column = len(self.data[0])

    def __str__(self):

        for i in range(1, len(self.data)):
            if len(self.data[i]) != len(self.data[i - 1]):
                return 'Строки и столбцы должны быть одного размера соотвественно!'

        for i in range(self.row):
            for j in range(self.column):
                print(str(self.data[i][j]).ljust(3), end=' ')
            print()
        return 'Вывод матрицы окончен!\n'

    def __add__(self, other):
        if len(self.data) != len(other.data):
            return 'Матрицы должны быть одного размера!'
        for i in range(len(self.data)):
            if len(self.data[i]) != len(other.data[i]):
                return 'Матрицы должны быть одного размера!'
        matrix = [[0]*self.column for _ in range(self.row)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(matrix)


my_matrix_1 = Matrix([[1, 1, 1], [1, 1, 1]])

my_matrix_2 = Matrix([[4, 4, 4], [4, 4, 4]])

my_matrix_3 = my_matrix_1 + my_matrix_2

print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_3)
