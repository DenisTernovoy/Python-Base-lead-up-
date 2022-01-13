profit = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

economic_result = profit - costs
if economic_result > 0:
    print('Фирма получает прибыль:', economic_result)
    profitability = economic_result / profit
    num_workers = int(input('Введите численность сотрудников фирмы: '))
    print('Прибыль фирмы в расчете на одного сотрудника:', economic_result / num_workers)
else:
    print('Фирма работает в убыток:', economic_result)

