with open("file_6.txt", 'r', encoding='utf-8') as file:
    my_dict = {}
    for line in file.readlines():
        subject = line[:line.index(':')]
        sentence = line[line.index(':')+1:].split()
        list_sum = []
        for word in sentence:
            number = ''
            for letter in word:
                if letter in '0123456789':
                    number += letter
            try:
                list_sum.append(int(number))
            except Exception:
                pass
        my_dict[subject] = sum(list_sum)

print(my_dict)
