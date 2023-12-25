import example_1


def test_serial_to_unique_id_0():
    assert example_1.serial_to_unique_id(0) is not None


def test_service_signal_0():
    assert example_1.service_signal('') is not None
