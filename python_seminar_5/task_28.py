def sum_of_nums(a, b):
    if a == 0:
        return b
    return sum_of_nums(a - 1, b + 1)

print(sum_of_nums(29, 74))