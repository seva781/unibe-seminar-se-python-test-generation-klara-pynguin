import example_2


def test_method_0():
    assert example_2.method(2, 1) == 4
    assert example_2.method(1, 0) == 5
    assert example_2.method(0, 1) == 5
    assert example_2.method(0, 0) == 6
