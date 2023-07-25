import pytest

pytestmark = [pytest.mark.smoke]  # run test a module level!


@pytest.mark.sanity
def test_makers_first_group():
    assert 'Cardinals' == 'Cardinals'


@pytest.mark.sanity
@pytest.mark.homolog
def test_makers_second_group():
    assert 1 + 1 == 2
    assert 10 * 8 == 80
    assert 28 - 6 == 22


def test_makers_third_group():
    assert 'Cardinals' == 'Cardinals'


@pytest.mark.sanity
def test_makers_fourth_group():
    assert 1 + 1 == 2
    assert 10 * 8 == 80
    assert 28 - 6 == 22
