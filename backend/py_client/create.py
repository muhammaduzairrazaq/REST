import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is create api view"
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
