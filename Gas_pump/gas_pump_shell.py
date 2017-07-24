import gas_pump_core, gas_disk

def main():
    inventory = gas_disk.tank_inven()
    print('Welcome to Brits Gas\n')
    payment = input('\nWould you like to pre-pay or pay after?\n')
    if payment == 'refuel':
        print(gas_pump_core.refuel())
        return None
    if payment == 'revenue':
        print('Your total revenue is ${:.2f}'.format(gas_pump_core.revenue()))
        return None

    gas_kind = input('\n(1) Regular $1.92, (2) Mid-Grade $2.00, (3) Premium $2.18\n')
    if payment == 'pre-pay' or 'prepay':
        dollars, gallons, gas_kind = gas_pump_core.prepay(gas_kind)

    elif payment == 'pay after':
        dollars, gallons, gas_kind = gas_pump_core.pay_after(gas_kind)
    
    msg = gas_pump_core.message_log(gas_kind, dollars, gallons) # writes the message for the log (str)
    gas_disk.log_file(msg) # writes the message to the log (file)
    if gas_pump_core.take_away(gas_kind, gallons, inventory):
        print('Successful sale!')
    
if __name__ == '__main__':
    main()
