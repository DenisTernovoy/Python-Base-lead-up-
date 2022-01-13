with open("file_2.txt", 'r') as file:
    counter = 0
    my_list = file.readlines()
    print(f"Всего строк: {len(my_list)}")
    print()
    for line in my_list:
        counter += 1
        print(f'{counter}-я строка состоит из {len(line.split())} слов')