# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
k = 0
for _ in range(n):
    opt = int(input())
    if opt == 1:
        k += 1
print(k if k < n / 2 else n - k)
