import core, disk


def input_password():
    while True:
        password = input('Please enter password to review checkins, or press Q to quit.\n')
        if password == 'Q':
            print('Goodbye!')
            exit()
        elif password == 'Jellyfish':
            break
        else:
            print('\nInvalid Password.')
            
def review_checkin(log, day):
    """([list], str) -> [list]"""
    check_ins = [] 
    for item in log:
        if day == item[2]:
            check_ins.append(item)
    return check_ins

def input_day():
    while True:
        day = input('\nHello Instructor!\n\nWould you like to look for a specific date? (Example: July-9)\n').title()
        if day == 'Q':
            print('Goodbye')
            exit()
        else:
            return day

def review_student(log, student):
    """([list], str) -> [list]"""
    names = [] 
    for item in log:
        if student == item[0]:
            names.append(item)
    return names


def input_student():
    while True:
        student = input('\nWould you like to look for a specific student? (Example: Britney)\n')
        if student == 'Q':
            print('Goodbye')
            exit()
        else:
            return student


# def review_log(name, time, date):
#     """([list], str) -> [list]"""
#     log = []
#     for item in name:
#         if name == item[0]:
#             log.append(item)
#         if time == item[1]:
#             log.append(item)
#         if date == item[2]:
#             log.append(item)
#     return log

def input_log():
    while True:
        log_2 = input('\n\nWould you like to review all checkins?\n')
        if log_2 == 'Q':
            print('Goodbye')
            exit()
        elif log_2 == 'yes':
            print(disk.open_inven())
            break
        else:
            return log_2

# def neat_list(list):
#     new = ''
#     for item in list:
#         ind = list.index(item)
#         # print(item, ind, '\n')
#         phrase = ("\n\t\t", str(ind + 1), ". ", str(list[ind][0]).capitalize(), ", ", (list[ind][1]), ", ",  str(list[ind][2]) )
#         for item in phrase:
#            new += (item)
#     return new

def main():
    log = disk.open_inven()
    while True:
        password = input_password()
        day = input_day()
        print(core.neat_list(review_checkin(log, day)))
        student = input_student()
        print(core.neat_list(review_student(log, student)))
        log_2 = input_log()
        # print(review_log(name, time, date))
        exit()
    else:
        print('Goodbye')
        exit()
if __name__ == '__main__':
    main()

