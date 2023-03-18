n = int(input('Введите размер массива: '))
nums = [i for i in range(1, n + 1)]
x = int(input('Введите число для сравнения с элементами массива: '))
min_val, min_ind = 10 ** 6, 0
for i in range(len(nums)):
    if abs(nums[i] - x) < min_val:
        min_val = abs(nums[i] - x)
        min_ind = i
print(nums[min_ind])
