def math_operations():
    operat = input('Введите арифметическую операцию: ')
    if operat == '0':
        print('Завершение программы')
    elif operat in '+-/*':
        try:
            a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
        except ValueError:
            print('Вы можете вводить только цифры')
            math_operations()
        if operat == '+':
            print(f'Сумма чисел = {a + b}')
            math_operations()
        elif operat == '-':
            print(f'Разность чисел = {a - b}')
            math_operations()
        elif operat == '*':
            print(f'Произведение чисел = {a * b}')
            math_operations()
        elif operat == '/':
            try:
                print(f'Частное чисел = {a / b}')
            except ZeroDivisionError:
                print('Нельзя делить на 0')
            math_operations()
    else:
        print('Вы ввели неверный знак операции')
        math_operations()

math_operations()
