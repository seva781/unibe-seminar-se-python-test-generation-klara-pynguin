# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Quicksort as module_0
import builtins as module_1


def test_case_0():
    dict_0 = {}
    var_0 = module_0.quicksort(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    bool_0 = False
    tuple_0 = (object_0, bool_0)
    module_0.quicksort(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x84\xe8\xb0\xa3\x1e\xe6p|\xa0\r\x90\xb7"
    module_0.quicksort(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.quicksort(none_type_0)