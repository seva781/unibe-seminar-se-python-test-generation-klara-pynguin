# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import helpers as module_0


def test_case_0():
    str_0 = '|\\^|o"VV8-/'
    none_type_0 = None
    str_1 = module_0.generate_url(str_0, none_type_0)
    assert str_1 == 'http://|\\^|o"VV8-:None/'
    str_2 = module_0.generate_url(str_0, str_0)
    assert str_2 == 'http://|\\^|o"VV8-:|\\^|o"VV8-//'


def test_case_1():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    str_0 = module_0.generate_url(dict_0, tuple_0)
    assert str_0 == "http://{(): ()}:()/"


def test_case_2():
    set_0 = set()
    list_0 = [set_0, set_0]
    bool_0 = True
    str_0 = module_0.generate_url(list_0, bool_0)
    assert str_0 == "http://[set(), set()]:True/"
    none_type_0 = None
    str_1 = module_0.generate_url(list_0, none_type_0)
    assert str_1 == "http://[set(), set()]:None/"
    dict_0 = {}
    str_2 = module_0.generate_url(dict_0, dict_0)
    assert str_2 == "http://{}:{}/"
    str_3 = module_0.generate_url(dict_0, dict_0)
    assert str_3 == "http://{}:{}/"
    none_type_1 = None
    str_4 = module_0.generate_url(str_3, none_type_1)
    assert str_4 == "http://{}:{}:None/"
    none_type_2 = None
    str_5 = module_0.generate_url(dict_0, none_type_2)
    assert str_5 == "http://{}:None/"


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.generate_url(none_type_0, none_type_0)
