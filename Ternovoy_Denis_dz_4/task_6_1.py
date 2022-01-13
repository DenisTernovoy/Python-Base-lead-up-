from itertools import count


start = 1

for i in count(start, 2):
    if i > 20:
        break
    print(i)
