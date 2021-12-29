def reg(**kwargs):
    DATA = []
    for i in kwargs:
        DATA.append(kwargs[i])
    return DATA

result = reg(name = input('Имя: '),
    surname = input('Фамилия: '),
    birth_year = input('Год рождения: '),
    city = input('Город проживания: '),
    email = input('Почта: '),
    phone_number = input('Телефонный номер: ')
)

print(*result, sep = ', ')