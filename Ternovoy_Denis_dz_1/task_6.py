result = int(input('Результат пробежки в первый день, км: '))
required_result = int(input('Желаемый результат (не менее), км: '))

day = 1
step = 0.1
print(day, 'день:', result)

while result < required_result:
    result *= 1.1
    day += 1
    print(day, 'день:', round(result, 2))
print()
print('На', day, 'день спортсмен достигнет результата - не менее', required_result, 'км.')