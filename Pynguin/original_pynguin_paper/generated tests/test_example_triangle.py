# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import example_triangle as module_0


def test_case_0():
    bool_0 = True
    str_0 = module_0.triangle(bool_0, bool_0, bool_0)
    assert str_0 == " Equilateral triangle "


def test_case_1():
    none_type_0 = None
    bool_0 = False
    str_0 = module_0.triangle(none_type_0, bool_0, bool_0)
    assert str_0 == " Isosceles triangle "


def test_case_2():
    str_0 = "[c!h"
    float_0 = 523.050252
    bool_0 = False
    int_0 = 2262
    bool_1 = False
    str_1 = module_0.triangle(bool_0, int_0, bool_1)
    assert str_1 == " Isosceles triangle "
    str_2 = module_0.triangle(str_0, str_0, float_0)
    assert str_2 == " Isosceles triangle "


def test_case_3():
    bytes_0 = b"\x01\xd1\xa5\x9e\x13\x13u\xd3\xc7\xb8\xab\x8b\xc4\x8d\x15\xbbJ\x9e\xd3"
    bool_0 = True
    none_type_0 = None
    str_0 = module_0.triangle(bytes_0, bool_0, none_type_0)
    assert str_0 == " Scalene triangle "
