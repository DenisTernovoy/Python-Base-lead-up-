with open("file_3.txt", 'r', encoding='utf-8') as file:
    my_list = []
    summ = 0
    counter = 0
    for string in file.readlines():
        name, salary = string.split()
        if int(salary) < 20000:
            my_list.append(name)
        summ += int(salary)
        counter += 1
    print(*my_list, sep='\n')
    print()
    print(f'Средний оклад: {summ / counter}')
