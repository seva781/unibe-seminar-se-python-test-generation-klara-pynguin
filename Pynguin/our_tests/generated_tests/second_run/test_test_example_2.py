# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import test_example_2 as module_0


def test_case_0():
    int_0 = 2880
    int_1 = 398
    var_0 = module_0.method(int_0, int_1)
    assert var_0 == 4


def test_case_1():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.method(bool_0, none_type_0)
    assert var_0 == 5


def test_case_2():
    str_0 = '\x0c&!kUb-"3RdOw~x['
    bool_0 = False
    var_0 = module_0.method(bool_0, str_0)
    assert var_0 == 5
    float_0 = -831.0
    var_1 = module_0.method(str_0, float_0)
    assert var_1 == 4
