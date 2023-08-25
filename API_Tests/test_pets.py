import pytest
from utils.utils import get_api_return_response_data
from utils.utils import time_limit_response_api

base_url = "https://petstore.swagger.io/v2/pet/"
pet_id = "8989"


@pytest.mark.currentTest
def test_get_by_id():
    url = base_url + pet_id
    data, resp_status, time_taken = get_api_return_response_data(url)
    performance = time_limit_response_api(time_taken)
    assert data['id'] == int(pet_id)
    assert resp_status == 200
    assert performance is True
