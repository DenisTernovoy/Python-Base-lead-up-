n = int(input())

maximum = 0

while n != 0:
    last_digit = n % 10
    if last_digit >= maximum:
        maximum = last_digit
    n = n // 10
print(maximum)