# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import Quicksort as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xd5\xe4\xa1\x1a|\x8d\xc3M\xa6\xeb\x9d=?\xaf\xf7C\xa5\x01z\xfc"
    module_0.quicksort(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Oi"
    list_0 = []
    object_0 = module_1.object(*list_0)
    list_1 = [str_0, str_0, str_0, object_0]
    module_0.quicksort(list_1)