def my_func(x, y):
    return x ** y


def my_func_1(x, y):
    total = 1
    for i in range(-y):
        total *= 1/x
    return total

try:
    x = int(input())
    y = int(input())
except ValueError:
    print('Введите число!')
else:
    print(round(my_func(x, y), 3))
    if y < 0:
        print(round(my_func_1(x, y), 3))
