import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"name":"uzair"})
print(get_response.text)