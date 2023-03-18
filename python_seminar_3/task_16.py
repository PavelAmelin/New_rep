n = int(input('Введите размер массива: '))
nums = [i for i in range(1, n + 1)]
x = int(input('Введите число для сравнения с элементами массива: '))
print(nums.count(x))