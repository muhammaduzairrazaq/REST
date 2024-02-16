import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Trying to update the first object.",
    "price": 1120.0
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
