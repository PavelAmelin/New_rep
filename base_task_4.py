revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print('Прибыль — выручка больше издержек')
    print(f'Финансовый результат - прибыль: {revenue - costs}')
    rentab = (revenue - costs) / revenue
    print(f'Рентабельность выручки: {rentab}')
    quant = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {(revenue - costs) / quant}')
else:
    print('Убыток — издержки больше выручки')
    print(f'Финансовый результат - убыток: {costs - revenue}')
