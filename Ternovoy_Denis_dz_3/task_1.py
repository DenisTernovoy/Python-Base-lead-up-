from datetime import datetime as D


dev_calc = lambda a, b: round(a / b, 2)

try:
    a = int(input('Введите делимое:\n'))
    b = int(input('Введите делитель:\n'))
except ValueError:
    print('Введите число!')
else:
    try:
        print(dev_calc(a, b))
    except ZeroDivisionError:
        print('Деление на 0 невозможно!')