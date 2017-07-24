def tank_inven():
    inventory = []
    with open('tank.txt', 'r') as file:
        file.readline()
        str_inventory = file.readlines()
    for item in str_inventory:
        sub_list = item.strip().split(', ')
        inventory.append([sub_list[0], sub_list[1], float(sub_list[2]), float(sub_list[3])])
    return inventory

def log_file(message):
    with open('log.txt', 'a') as file:
        file.write(message)
    return message

def in_the_log():
    inventory = []
    with open('log.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return inventory