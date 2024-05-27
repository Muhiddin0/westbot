import requests

BASE_URL = "http://127.0.0.1:8000"

def create_user(user):
    url = f"{BASE_URL}/bot/users/"
    return requests.post(url, json=user).json()

def getUser(user_id):
    url = f"{BASE_URL}/bot/users/" + str(user_id)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False

def getCategorys():
    url = f"{BASE_URL}/food/category/"
    return requests.get(url).json()