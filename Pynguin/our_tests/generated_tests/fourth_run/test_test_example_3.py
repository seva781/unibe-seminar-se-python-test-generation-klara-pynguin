# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import test_example_3 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.sorting(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 50
    bytes_0 = b""
    tuple_0 = (int_0, int_0, bytes_0)
    module_0.sorting(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    int_0 = 1496
    int_1 = -171
    int_2 = 2176
    list_0 = [int_0, int_1, int_0, int_2]
    var_0 = module_0.sorting(list_0)
    module_0.sorting(none_type_0)
