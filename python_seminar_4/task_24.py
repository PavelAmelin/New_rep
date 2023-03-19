n = int(input('Введите количество кустов: '))
all_blueb = []
for i in range(1, n + 1):
    blueb_quant = int(input(f'Введите количество ягод с {i} куста: '))
    all_blueb.append(blueb_quant)
res = [all_blueb[0] + all_blueb[1] + all_blueb[-1]]
for i in range(1, len(all_blueb) - 1):
    res.append(sum(all_blueb[i - 1:i + 2]))
res.append(all_blueb[0] + all_blueb[-1] + all_blueb[-2])
print(max(res))
