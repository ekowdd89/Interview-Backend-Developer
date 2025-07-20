import requests


def get_products():
    try:
        response = requests.get("http://127.0.0.1:8001/api/v1/products")
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
def post_product(product):
    try:
        response = requests.post("http://127.0.0.1:8001/api/v1/products", json={
            "name": product['name'],
            "price": product['price'],
            "quantity": product['quantity']
        })
        response.raise_for_status()
        if response.status_code == 201:
            data = response.json()
            return data
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
def update_product(product, product_id):
    try:
        response = requests.put(f"http://127.0.0.1:8001/api/v1/products/{product_id}", json={
            "name": product['name'],
            "price": product['price'],
            "quantity": product['quantity']
        })
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
def get_product(product_id):
    try:
        response = requests.get(f"http://127.0.0.1:8001/api/v1/products/{product_id}")
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    
def delete_product(product_id):
    try:
        response = requests.delete(f"http://127.0.0.1:8001/api/v1/products/{product_id}")
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []