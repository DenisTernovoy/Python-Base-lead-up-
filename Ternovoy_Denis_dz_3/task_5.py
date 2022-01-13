summ = 0


# '*' - специальный символ


flag = True
while flag:
    numbers = input().split()
    for i in numbers:
        if i != '*':
            summ += int(i)
        else:
            flag = False
            break
    print(summ)