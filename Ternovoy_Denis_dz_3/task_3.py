def my_func(num_1, num_2, num_3):
    return sum([num_1, num_2, num_3]) - min(num_1, num_2, num_3)

a = int(input('Введите 1-е число:\n'))
b = int(input('Введите 2-e число:\n'))
c = int(input('Введите 3-е число:\n'))

print(my_func(a, b, c))
