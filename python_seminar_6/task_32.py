# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def all_index_between():
    try:
        min_val = int(input('Введите минимум диапазона: '))
        max_val = int(input('Введите максимум диапазона: '))
        lst = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
        print(*[i for i in range(len(lst)) if min_val <= lst[i] <= max_val])
    except ValueError:
        print('Вводить можно только числа')
        all_index_between()

all_index_between()
