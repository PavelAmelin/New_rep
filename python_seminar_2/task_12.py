x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if i + j == x and i * j == y:
            print(i, j)

