import pytest
from utils.utils import get_api_return_response_data, put_api_update_data,delete_api_data
from utils.utils import time_limit_response_api
from utils.env_configparser import get_pet_env_qa

import logging


LOGGER = logging.getLogger(__name__)

base_url = get_pet_env_qa()
pet_id = "8989"


@pytest.mark.currentTest
def test_get_by_id():
    url = base_url + pet_id
    data, resp_status, time_taken = get_api_return_response_data(url)
    LOGGER.info("API call Done!!!")
    performance = time_limit_response_api(time_taken)
    assert data['id'] == int(pet_id)
    assert resp_status == 200
    assert performance is True


def test_update_by_id():
    url = base_url
    payload = {"id": int(pet_id), "name": "test automation", "status": "pending"}
    data, resp_status, time_taken = put_api_update_data(url, payload)
    performance = time_limit_response_api(time_taken)
    print("Update data: ", data)
    assert data['id'] == int(pet_id)
    assert data['name'] == 'test automation'
    assert data['status'] == 'pending'
    assert performance is True


def test_delete_by_id():
    url = base_url + pet_id
    api_key = {'api_key': 'apikeys123'}
    data, resp_status, time_taken = delete_api_data(url, api_key)
    performance = time_limit_response_api(time_taken)
    print("Delete data: ", data)
    assert data['message'] == pet_id
    assert data['code'] == 200
    assert performance is True
