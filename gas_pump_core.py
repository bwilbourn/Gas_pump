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

def pay_after(gallons, price):
    """ 
    """
    dollars = gallons * price 
    message = '\nYour total is: ${}'.format(round(dollars, 2))
    return [dollars, message]
    
    
def prepay(money, price):
    """
    """
    gallons = money / price
    msgg = '\nYour total amount of gallons purchased: ${}'.format(round(gallons, 2))
    return [gallons, msgg]

def message_log(gas_kind, gallons, dollars):    
    if gas_kind == '1' or gas_kind == 'one':
        gas_kind = 'regular' 
    elif gas_kind == '2' or gas_kind == 'two':
        gas_kind = 'mid-Grade'
    elif gas_kind == '3' or gas_kind == 'three':
        gas_kind = 'premium'
    return '{}, {}, {}\n'.format(gas_kind, dollars, gallons)


def take_away(gas_kind, gallons, inventory):
    str_l = ['code, type, amount_in_inventory, price']
    for item in inventory:
        if item[0] == gas_kind:
            item[2] = item[2] - gallons
        str_l.append('{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))
        message = '\n'.join(str_l)
    return True


def refuel(inventory):
    # Sean's cheating way
    # str_l = ['code, type, amount_in_inventory, price',
    # '1, regular, 5000.0, 1.92',
    # '2, mid-grade, 5000.0, 2.0',
    # '3, premium, 5000.0, 2.18'
    # ]
    str_l = ['code, type, amount_in_inventory, price']
    for item in inventory:
        if item[2] <= 2500.0:
            item[2] = 5000.0
        item[2] = str(item[2])
        item[3] = str(item[3])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)
    return message 

def revenue(inventory):
    price = 0 
    for item in inventory:
        price += item[2]
    return price 



    
    



