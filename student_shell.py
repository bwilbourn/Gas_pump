import core, disk

def input_name():
    while True:
        name = input('Please enter your name. Press Q to Quit.\n').title()
        if name == 'Q':
            print('Goodbye')
            exit()
        else:
            return name

def input_time():
    while True:
        time = input('What time are you checking in?\n')
        if time == 'q':
            print('Goodbye')
            exit()
        if ":" not in time:
            print('Not valid, please try again.')
            exit()
        else:
            return time

def input_date():
    while True:
        date = input('\nPlease input the date. \nExample: July-12\n\n')
        if date == 'q':
            print('Goodbye')
            exit()
        if '-' not in date:
            print('Not valid, please try again.')
            exit()
        else:
            return date


def main():
    while True:
        name = input_name()
        time = input_time()
        date = input_date()
        disk.append_log(name, time, date)
        exit()
    
if __name__ == '__main__':
    main()