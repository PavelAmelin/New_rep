num = int(input('Введите трехзначное число: '))
s = 0
while num > 0:
    s += num % 10
    num //= 10
print(f'Сумма цифр трехначного числа: {s}')
