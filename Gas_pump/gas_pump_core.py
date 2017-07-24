def gas_price(gas_kind):
    """This was made by Britney in Base Camp
    """
    if gas_kind == '1' or gas_kind == 'one':
        return 1.92
    elif gas_kind == '2' or gas_kind == 'two':
        return 2.00
    elif gas_kind == '3' or gas_kind == 'three':
        return 2.18
    return False

def pay_after(gas_kind):
    """ 
    """
    gallons = float(input('\nHow many gallons would you like to purchase?\n'))
    price = gas_price(gas_kind)
    dollars = gallons * price 
    print('\nYour total is: $', round(dollars, 2),sep='')
    return [dollars, gallons, gas_kind]
    
    
def prepay(gas_kind):
    """
    """
    money = float(input('\nHow much money would you like to spend?\n'))
    price = gas_price(gas_kind)
    gallons = money / price
    print('\nYour total amount of gallons purchased:\n', round(gallons, 2))
    return [money, gallons, gas_kind]

def message_log(gas_kind, gallons, dollars):    
    if gas_kind == '1' or gas_kind == 'one':
        gas_kind = 'regular' 
    elif gas_kind == '2' or gas_kind == 'two':
        gas_kind = 'mid-Grade'
    elif gas_kind == '3' or gas_kind == 'three':
        gas_kind = 'premium'
    return = '{}, {}, {}\n'.format(gas_kind, dollars, gallons)


def take_away(gas_kind, gallons, inventory):
    str_l = ['code, type, amount_in_inventory, price']
    for item in inventory:
        if item[0] == gas_kind:
            item[2] = item[2] - gallons
        str_l.append('{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))
        message = '\n'.join(str_l)
    with open('tank.txt', 'w') as file:
        file.write(message)
    return True


def refuel():
    # Sean's cheating way
    # str_l = ['code, type, amount_in_inventory, price',
    # '1, regular, 5000.0, 1.92',
    # '2, mid-grade, 5000.0, 2.0',
    # '3, premium, 5000.0, 2.18'
    # ]
    str_l = ['code, type, amount_in_inventory, price']
    inventory = tank_inven()
    for item in inventory:
        if item[2] <= 2500.0:
            item[2] = 5000.0
        item[2] = str(item[2])
        item[3] = str(item[3])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)
        
    with open('tank.txt', 'w') as file:
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

def revenue():
    inventory = in_the_log()
    price = 0 
    for item in inventory:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price 



    
    



