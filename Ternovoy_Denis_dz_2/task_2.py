my_list = [input('Введите элемент:\n') for i in range(int(input('Колличество введений: ')))]
print(*my_list, sep = ', ')

for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(*my_list, sep = ', ')
