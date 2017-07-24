import core, disk

def main():
    while True:
        name = core.input_name()
        time = core.input_time()
        date = core.input_date()
        disk.append_log(name, time, date)
        exit()
    
if __name__ == '__main__':
    main()