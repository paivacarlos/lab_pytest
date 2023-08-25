import requests, json


def get_api_return_response_data(url):
    header = {'Content-Type': 'application/json'}
    print("Request URL: ", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    assert len(data) > 0, "Empty response!!!"
    return data, response.status_code, time_taken


def time_limit_response_api(time_taken):
    if time_taken > 5:
        return print("Time limit exceeded! Time taken: ", time_taken)
    else:
        return True