with open("file_5.txt", 'w') as file:
    numbers = input()
    file.write(numbers)
    numbers = [int(num) for num in numbers.split()]
    print(sum(numbers))