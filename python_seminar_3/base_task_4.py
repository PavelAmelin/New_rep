# def my_func(*args):
#     lst_arg = [i for i in args]
#     lst_arg.sort()
#     return lst_arg[-2] + lst_arg[-1]

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
