# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

class OurRangeError(Exception):
    pass

def guess(n=50, k=1, mid=50):
    print(f'вводим число {n}, наша {k} попытка')
    if n == my_num and k <= 10:
        print(f'угадано с {k} попытки')
    elif k > 10:
        print(f'не угадали число {my_num}')
    else:
        if n < my_num:
            guess(n + mid, k + 1, mid // 2 if mid // 2 > 0 else 1)
        else:
            guess(n - mid, k + 1, mid // 2 if mid // 2 > 0 else 1)


while True:
    try:
        my_num = int(input('Введите загаданное число от 0 до 100: '))
        if not 0 <= my_num <= 100:
            raise OurRangeError('Вводить нужно только от 0 до 100')
        guess()
    except OurRangeError as e:
        print(e)
        continue
    break
