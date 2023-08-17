import pytest

@pytest.mark.parametrize('test_input', [28, 89, 22, 34])
def test_param_01(test_input):
    assert test_input > 50
