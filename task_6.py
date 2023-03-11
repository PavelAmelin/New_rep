num = int(input('Введите шестизначный номер: '))
sum_start, sum_end = 0, 0
while num > 1000:
    sum_end += num % 10
    num //= 10
while num > 0:
    sum_start += num % 10
    num //= 10
print('yes' if sum_start == sum_end else 'no')
