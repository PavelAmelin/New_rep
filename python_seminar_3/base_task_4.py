# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:

#  1) используя функцию sort()

def my_func(*args):
    lst_arg = [i for i in args]
    lst_arg.sort()
    return lst_arg[-2] + lst_arg[-1]

# 2) без функции sort()

def my_func(*args):
    lst_arg = [i for i in args]
    max_val, premax_val = 0, 0
    for i in lst_arg:
        if i > max_val:
            premax_val = max_val
            max_val = i
        elif i > premax_val and i < max_val:
            premax_val = i
    return premax_val + max_val

print(my_func(15, 50, 20))
