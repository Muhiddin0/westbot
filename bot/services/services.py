import requests

BASE_URL = "http://127.0.0.1:8000"

def createUser(user):
    url = f"{BASE_URL}/bot/users/"

    response = requests.post(url, data=user)
    print(response.json())
    
    return response.json()

def getUser(user_id):
    url = f"{BASE_URL}/bot/users/" + str(user_id)
    response = requests.get(url)
    
    print(response)
    print(response.json())

    if response.status_code == 200:
        return response.json()

    return False

def getCategorys():
    url = f"{BASE_URL}/foods/category/"
    return requests.get(url).json()

def getFoods(category):
    url = f"{BASE_URL}/foods/category/{category}/"

    return requests.get(url).json()