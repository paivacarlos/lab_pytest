def test_name_is_equal():
    print("I would like to see my print!")  # pytest -v -s / pytest -v --exitfirst
    assert 'Cardinals' == 'Cardinals'


def test_arithmetic():
    assert 1 + 1 == 2
    assert 10 * 8 == 80
    assert 28 - 6 == 22
