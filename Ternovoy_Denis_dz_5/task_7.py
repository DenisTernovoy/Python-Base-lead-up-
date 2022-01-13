import json

with open("file_7.txt", 'r') as file:
    base = 0
    counter = 0
    finish_list = []
    my_dict = {}
    for line in file.readlines():
        my_list = line.split()
        name = my_list[0]
        profit = int(my_list[2]) - int(my_list[3])
        my_dict[name] = profit
        if profit > 0:
            base += profit
            counter += 1
    average_profit = {'average_profit': round(base / counter, 2)}
    finish_list.append(my_dict)
    finish_list.append(average_profit)
    with open("json_file.json", 'w') as file_json:
        json.dump(finish_list, file_json)


