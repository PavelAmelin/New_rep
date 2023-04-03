class Road:

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weigth(self, m, depth):
        self.m = m
        self.depth = depth
        print(f'{int(self._width * self._length * m * depth)} кг')

res = Road(width=20, length=5000)
res.weigth(m=25, depth=0.05)


