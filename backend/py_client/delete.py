import requests
product_id = input("Enter product id: ")
try:
    product_id = int(product_id)
except:
    print("Invalid product id")

if product_id:

    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
