import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is create api view"
}

get_response = requests.get(endpoint)
print(get_response.json())
