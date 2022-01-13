<<<<<<< HEAD
GOODS = []

flag = True
count = 1

while flag:
    good = []
    good.append(count)
    description = {
        'Название': input('Введите название товара:\n'),
        'Количество': int(input('Введите количество товара:\n')),
        'Цена': int(input('Введите цену товара:\n')),
        'Ед': input('Введите единицу измерения:\n')
    }
    good.append(description)
    GOODS.append(tuple(good))
    request_exit = input('Желаете добавить еще один товар? (да/любой символ)\n')
    if request_exit.lower() == 'да':
        count += 1
    else:
        print('Добавление товаров прекращено!')
        flag = False

DATA = {
    'Название':[],
    'Количество': [],
    'Цена': [],
    'Ед': []
}

for i in GOODS:
    DATA['Название'].append(i[1]['Название'])
    DATA['Количество'].append(i[1]['Цена'])
    DATA['Цена'].append(i[1]['Количество'])
    DATA['Ед'].append(i[1]['Ед'])

print(DATA)
=======
def int_func(string):
    return string.title()


words = input()
print(int_func(words))

>>>>>>> DZ_3
