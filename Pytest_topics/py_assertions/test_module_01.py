
def test_different_assert():
    assert 28 != 89


def test_boolean_assert():
    assert 1
    assert True


def test_strings_assert():
    assert "qwer" == 'qwer'


def test_precedence_assert():
    assert ((3-1)*4/2) == 4


def test_in_assert():
    assert 0 in divmod(10, 2)
    assert 1 in divmod(9, 5)
    assert "is" in "this is pytest"
    assert "or" not in "this is pytest"
    assert 23 in [29, 22, 89, 23, 7]
