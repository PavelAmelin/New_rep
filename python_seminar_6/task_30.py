n = int(input('Введите количество элементов прогрессии: '))
a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность элементов: '))
progression = [(a1 + i) for i in range(0, d * n, d)]
print(progression)