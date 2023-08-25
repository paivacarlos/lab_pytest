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


def test_get_pet_by_id():
    url = base_url + pet_id
    header = {'Content-Type': 'application/json'}
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))

    assert data['id'] == 8989
    assert data['name'] == "doggie"


def test_get_post_new_pet():
    url = base_url
    header = {'Content-Type': 'application/json'}
    payload = {"id": 2801, "name": "swan", "status": "available"}
    response = requests.post(url, verify=True, json=payload, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))

    assert data['id'] == 2801
    assert data['name'] == 'swan'
    assert data['status'] == 'available'
