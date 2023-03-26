def in_power(a, b):
    if b == 0:
        return 1
    return a * in_power(a, b - 1)

print(in_power(3, 3))
