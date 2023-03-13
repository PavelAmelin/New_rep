n = int(input('Введите количество монет: '))
k = 0
for _ in range(n):
    opt = int(input())
    if opt == 1:
        k += 1
print(k if k < n / 2 else n - k)
