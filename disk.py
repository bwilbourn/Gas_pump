def append_log(name, time, date):
    '''str, str, str -> str
    adds to checkins.txt with every input.
    '''
    with open('checkins.txt', 'a') as file:
        file.write(str(name) + " , " + str(time) + " , " + str(date) + "\n")