revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
quant = int(input('Введите численность сотрудников фирмы: '))
income = revenue - costs
rentab = income / revenue
unit_income = income / quant
print(f'Финансовый результат - прибыль: {income}')
print(f'Рентабельность выручки: {rentab}')
print(f'Прибыль фирмы в расчете на одного сотрудника: {unit_income}')