from itertools import cycle


my_list = [1, 2, 3, 4, 5]
count = 0

for i in cycle(my_list):
    if count > 8:
        break
    count += 1
    print(i)
