# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество монет: '))
k = 0
for _ in range(n):
    opt = int(input())
    if opt == 1:
        k += 1
print(k if k < n / 2 else n - k)
