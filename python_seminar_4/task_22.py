m, n = int(input('Введите размер первого массива: ')), int(input('Введите размер второго массива: '))
lst_1 = [int(input()) for _ in range(m)]
lst_2 = [int(input()) for _ in range(n)]
print(sorted(set(lst_1) & set(lst_2)))
