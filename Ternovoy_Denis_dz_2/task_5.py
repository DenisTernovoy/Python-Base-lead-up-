my_list = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг: {my_list}')

flag = True
while flag:
    try:
        new_element = int(input('Введите число:\n'))
        flag = False
    except ValueError:
        print('Неверный ввод!')

my_list.append(new_element)
print('Текущий рейтинг: {}'.format(sorted(my_list, reverse= True)))
