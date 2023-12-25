import example_3


def test_method_0():
    assert example_3.method(True, True) == 4
    assert example_3.method(True, False) == 5
    assert example_3.method(False, True) == 5
    assert example_3.method(False, False) == 6
