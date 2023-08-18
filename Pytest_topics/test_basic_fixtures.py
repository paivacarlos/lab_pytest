import pytest


@pytest.fixture()
def setup_city_list():
    print("\n Here is starting the fixture! \n")
    city = ["Porto Alegre", "São Leopoldo", "Evora", "Lisboa", "Porto"]
    return city


def test_get_item(setup_city_list):
    print(f"Here, we are printing the cities: {setup_city_list[1:3]}")
    assert setup_city_list[0] == "Porto Alegre"
    assert setup_city_list[::2] == ["Porto Alegre", "Evora", "Porto"]
