n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Введите колиечство долей: '))
if k % m == 0 or k % n == 0:
    print('yes')
else:
    print('no')
