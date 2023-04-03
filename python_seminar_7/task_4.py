class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        res = ''
        for row in self.matr:
            for i in row:
                res += str(i) + ' '
            res += '\n'
        return res

    def __add__(self, other):
        try:
            result = self.matr.copy()
            for i in range(len(self.matr)):
                for j in range(len(self.matr[i])):
                    result[i][j] = self.matr[i][j] + other.matr[i][j]
            return Matrix(result)
        except IndexError:
            return 'Введите матрицы одной длины и ширины'

a1 = Matrix([[231, 44, 3], [334, 54, 45]])
a2 = Matrix([[132, 211, 411], [531, 434, 1313]])
print(a1 + a2)
