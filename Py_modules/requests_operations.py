import json

import requests

base_url_to_get = 'https://httpbin.org/get'
my_params = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(base_url_to_get, params=my_params)
print(r.url)
print(r.headers)

for key, value in r.json().items():
    print(key, ":", value)

#  print data inside the json response
print(r.json()["headers"]["Host"])
#  assert the data
if r.json()["headers"]["Host"] == "httpbin.org":
    print(True)

base_url_to_post = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
my_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
r = requests.post(base_url_to_post, json=payload, headers=my_headers)
print(r.url)
print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)
