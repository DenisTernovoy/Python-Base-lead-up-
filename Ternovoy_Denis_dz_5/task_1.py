with open ("file_1.txt", 'w') as file:
    a = input()
    while a:
        file.write(a + '\n')
        a = input()