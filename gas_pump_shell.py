import gas_pump_core, gas_disk

def main():
    inventory = gas_disk.tank_inven()
    print('Welcome to Brits Gas\n')
    payment = input('\nWould you like to pre-pay or pay after?\n')
    # administrator options
    if payment == 'refuel':
        print(gas_pump_core.refuel(inventory))
        exit()
    elif payment == 'revenue':
        print('Your total revenue is ${:.2f}'.format(gas_pump_core.revenue(inventory)))
        exit()
    # customer options
    gas_kind = input('\n(1) Regular $1.92, (2) Mid-Grade $2.00, (3) Premium $2.18\n')
    if payment == 'pre-pay' or 'prepay':
        gallons = float(input('\nHow many gallons would you like to purchase?\n'))
        price = gas_pump_core.gas_price(gas_kind)
        dollars, msg = gas_pump_core.prepay(gallons, price)
        print(msg)
    elif payment == 'pay after':
        money = float(input('\nHow much money would you like to spend?\n'))
        price = gas_pump_core.gas_price(gas_kind)
        dollars, msgg = gas_pump_core.pay_after(gallons, price)
        print(msgg)
    msg = gas_pump_core.message_log(gas_kind, dollars, gallons) # writes the message for the log (str)
    gas_disk.log_file(msg) # writes the message to the log (file)
    if gas_pump_core.take_away(gas_kind, gallons, inventory):
        print('Successful sale!')
    
if __name__ == '__main__':
    main()
