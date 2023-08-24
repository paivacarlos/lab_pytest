import requests, json

import pytest

base_url = "https://petstore.swagger.io/v2/pet/"
pet_id = "8989"


def test_get_pet_check_response():
    url = base_url + pet_id
    header = {'Content-Type': 'application/json'}
    print("Request URL: ", url )
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(data)
    print(json.dumps(data, indent=3))
    assert len(data) > 0, "empty response"


@pytest.mark.currentTest
def test_get_pet_by_id():
    url = base_url + pet_id
    header = {'Content-Type': 'application/json'}
    print("Request URL: ", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))

    assert data['id'] == 8989
    assert data['name'] == "doggie"
