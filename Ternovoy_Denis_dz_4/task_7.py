def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        yield total


for el in fact(3):
    print(el)
