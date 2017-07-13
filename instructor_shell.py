import disk

def input_password():
    while True:
        password = input('Hello Instructor! Please enter password, or press Q to quit.\n')
        if password == 'Jellyfish':
            return None
        elif password == 'Q':
            print('Goodbye!')
            exit()
        else:
            ('\nInvalid Password.')
            exit()

