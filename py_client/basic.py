import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, params={'abc': 123}, json={'query': 'Hello world'}) # HTTP Request
# print(get_response.text.encode('utf-8')) # print raw text response
# print(get_response.status_code)

# print(get_response.json()['message'])
print(get_response.headers)
print(get_response.json())
print(get_response.status_code)
