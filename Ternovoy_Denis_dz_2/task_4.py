sentence = input('Введите предложение из слов, разделенных пробелами:\n')

num = 0
for i in sentence.split():
    num += 1
    print(f'{num} строка - {i[:10]}')
