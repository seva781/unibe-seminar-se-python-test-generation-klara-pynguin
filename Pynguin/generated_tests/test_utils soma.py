# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import utils as module_0


def test_case_0():
    dict_0 = {}
    bool_0 = module_0.is_api_response_success(dict_0)
    assert bool_0 is False


def test_case_1():
    str_0 = "result"
    dict_0 = {str_0: str_0}
    bool_0 = module_0.is_api_response_success(dict_0)
    assert bool_0 is False
    bool_1 = module_0.is_api_response_success(dict_0)
    assert bool_1 is False
    bool_2 = module_0.is_api_response_success(dict_0)
    assert bool_2 is False