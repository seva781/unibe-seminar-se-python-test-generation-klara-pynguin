# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import utils as module_0


def test_case_0():
    bool_0 = True
    int_0 = module_0.brightness_to_rflink(bool_0)
    assert int_0 == 0
    int_1 = -2766
    int_2 = module_0.brightness_to_rflink(int_1)
    assert int_2 == -162


def test_case_1():
    bool_0 = False
    int_0 = module_0.rflink_to_brightness(bool_0)
    bool_1 = False
    int_1 = module_0.brightness_to_rflink(bool_1)
    int_2 = -3120
    int_3 = module_0.brightness_to_rflink(int_2)
    assert int_3 == -183
