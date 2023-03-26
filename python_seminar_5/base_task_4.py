def sum_progression(n, k):
    if k == 0:
        return 0
    return n + sum_progression(n * (-0.5), k - 1)

quant = int(input('Введите количество первых элементов: '))
print(sum_progression(1, quant))
