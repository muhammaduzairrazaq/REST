import requests

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    "title": "Updating the data using the mixin view",
    "price": 1120.0
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
