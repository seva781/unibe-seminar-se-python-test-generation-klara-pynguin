# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import test_example_3 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1515
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.sorting(list_0)
    int_1 = 3608
    module_0.sorting(int_1)


def test_case_1():
    list_0 = []
    var_0 = module_0.sorting(list_0)


def test_case_2():
    int_0 = -524
    int_1 = 2328
    bool_0 = True
    list_0 = [int_0, int_1, bool_0]
    var_0 = module_0.sorting(list_0)
