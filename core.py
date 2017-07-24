def input_name():
    students = ['Maegan', 'Britney', 'Allie', 'Sara', 'Angel', 'Ozvaldo', 'Lisa', 'Jose', 'Timothy', 'Shedlia', 'Jo tavious', 'Edgar', 'Austin', 'Shay', 'Trey', 'Valentae', 'Asia']
    while True:
        name = input('Please enter your name. Press Q to Quit.\n').title()
        if name == 'Q':
            print('Goodbye')
            exit()
        elif name in students:
            break
        else:
            print('\nInvalid name, not a student.')
    return name

def is_time(time):
    """ str -> bool 
    >>> is_time('12:00')
    True
    >>> is_time('2:39')
    True
    >>> is_time('5')
    False
    >>> is_time('now')
    False
    >>> is_time('16:29')
    True
    >>> is_time('4:29 pm')
    False
    """
    if ':' not in time:
        return False
    hours, minutes = time.split(':')
    if not(hours.isdigit() and minutes.isdigit()):
        return False
    if int(hours) >= 0 and int(hours) < 24 and int(minutes) >= 0 and int(minutes) < 60:
        return True
    return False

def input_time():
    while True:
        time = input('What time are you checking in?\n')
        if time == 'q':
            print('Goodbye')
            exit()
        elif is_time(time):
            break
        else:
            print('Not valid, please try again.')
    return time

def days(month):
    if month == 'January':
        return 31
    elif month == 'February':
        return 28
    elif month == 'March':
        return 31
    elif month == 'April':
        return 30
    elif month == 'May':
        return 31
    elif month == 'June':
        return 30
    elif month == 'July':
        return 31
    elif month == 'August':
        return 31
    elif month == 'September':
        return 30
    elif month == 'October':
        return 31
    elif month == 'November':
        return 30
    elif month == 'December':
        return 31
    else:
        return 'Invalid' 
        

def is_date(date):
    """ str -> bool
    >>> is_date('January-2')
    True
    >>> is_date('1-2')
    False
    >>> is_date('September-25')
    True
    >>> is_date('March 9')
    False
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if '-' not in date:
        return False
    month, day = date.split('-')
    if not day.isnumeric():
        return False
    if month in months and int(day) <= days(month):
        return True
    return False

def input_date():
    while True:
        date = input('\nPlease input the date. \nExample: July-12\n\n')
        if date == 'q':
            print('Goodbye')
            exit()
        elif is_date(date):
            break
        else:
            print('Not valid, please try again.')
    return date
# neat_list needs to be on line 106 when I get it working.



# def neat_list(list):
#     new = ''
#     for item in list:
#         ind = list.index(item)
#         # print(item, ind, '\n')
#         phrase = ("\n\t\t", str(ind + 1), ". ", str(list[ind][0]).capitalize(), ", ", (list[ind][1]), ", ",  str(list[ind][2]) )
#         for item in phrase:
#            new += (item)
#     return new

