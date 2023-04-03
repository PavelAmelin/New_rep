class Road:
    m = 25
    depth = 0.05

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weigth(self):
        print(f'{int(self._width * self._length * self.m * self.depth)} кг')

res = Road(width=20, length=5000)
res.weigth()


