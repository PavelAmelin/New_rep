def even_uneven(n, ev=0, unev=0):
    if n == 0:
        return ev, unev
    else:
        if n % 10 % 2 == 0:
            ev += 1
        else:
            unev += 1
        return even_uneven(n // 10, ev, unev)

num = int(input('Введите число: '))
print(f'Количество четных и нечетных цифр: {even_uneven(num)}')
