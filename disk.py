def append_log(name, time, date):
    '''str, str, str -> str
    adds to checkins.txt with every input.
    '''
    with open('checkins.txt', 'a') as file:
        file.write(str(name) + " , " + str(time) + " , " + str(date) + "\n")
        
# def open_inven():
#     """opens inventory and splits it."""
#     new_inven = []
#     with open ('checkins.txt', 'r') as file:
#         file.readline()
#         inventory = file.readlines()
#     for item in inventory:
#         item1, quantity, price = item.split(', ')
#         new_inven.append([item1.strip(), str(quantity.strip()), str(price.strip())])
#     return new_inven 


def open_check_ins():
    """opens inventory and splits it."""
    check_in_information = []
    with open ('checkins.txt', 'r') as file:
        key_1, key_2, key_3 = file.readline().strip().split(', ')
        checkins = file.readlines()
    for item in checkins:
        name, time, date = item.strip().split(', ')
        check_in_information.append({key_1: name, key_2: time, key_3: date})
    print(check_in_information)
    return check_in_information



 
















