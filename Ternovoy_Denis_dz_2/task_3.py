my_dict = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]
}

month = int(input())

for i in my_dict.keys():
    if month in my_dict[i]:
        print(i)
