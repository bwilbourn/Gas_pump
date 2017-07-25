import gas_pump_core


def test_gas_price():
    assert gas_pump_core.gas_price('1') == 1.92
    assert gas_pump_core.gas_price('2') == 2.00
    assert gas_pump_core.gas_price('3') == 2.18
    assert gas_pump_core.gas_price('4') == False

def test_message_log():
    assert gas_pump_core.message_log('regular', 50.0, 26.04) == 'regular, 26.04, 50.0\n'
    assert gas_pump_core.message_log('mid-Grade', 65.0, 32.5) == 'mid-Grade, 32.5, 65.0\n'
    assert gas_pump_core.message_log('premium', 10.0, 21.8) == 'premium, 21.8, 10.0\n'
    assert gas_pump_core.message_log('a', 1, 2.0) != 'a, 1, 2.0\n' 
    assert gas_pump_core.message_log('a', 2.0, 1) == 'a, 1, 2.0\n'


def test_revenue():
    l = [
        ['a', 'b', 10],
        ['a', 'b', 20],
    ]
    assert gas_pump_core.revenue(l) == 30
    l = [
        ['a', 'b', 1.1],
        ['a', 'b', 2.2],
        ['a', 'b', 3.3],
    ]
    assert gas_pump_core.revenue(l) == 6.6


def test_pay_after():
    assert gas_pump_core.pay_after(20, 2.00) == [40.0, '\nYour total is: $40.0']


def test_prepay():
    assert gas_pump_core.prepay(20, 2.00) == [10.0, '\nYour total amount of gallons purchased: $10.0']