def divis(fir_num, sec_num):
    return fir_num / sec_num

try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(divis(a, b))
except ZeroDivisionError:
    print('Вы что? Пытаетесь делить на 0!')


