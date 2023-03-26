def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

num = int(input('Введите максимальное число ряда: '))
print(sum_numbers(num) == num * (num + 1) / 2)

