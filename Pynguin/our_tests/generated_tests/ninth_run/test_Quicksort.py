# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "si5"
    module_0.quicksort(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.quicksort(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"!O\xc0\t\x84\x8c\xe2+n"
    module_0.quicksort(bytes_0)
