import gas_pump_core


def test_gas_price():
    assert gas_pump_core.gas_price('1') == 1.92
    assert gas_pump_core.gas_price('2') == 2.00
    assert gas_pump_core.gas_price('3') == 2.18

