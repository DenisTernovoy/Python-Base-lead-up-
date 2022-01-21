with open("file_4.txt", 'r', encoding='utf-8') as file:
    my_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }
    new_file = open("file_4.2.txt", 'w')
    for line in file.readlines():
        sentence = line.split('—')
        new_file.write(f'{my_dict[sentence[0].strip()]} — {sentence[1]}')
    new_file.close()