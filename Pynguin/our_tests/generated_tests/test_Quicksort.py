# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Quicksort as module_0


def test_case_0():
    list_0 = []
    var_0 = module_0.quicksort(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ">IUjrBV:xy^"
    module_0.quicksort(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.quicksort(bool_0)
