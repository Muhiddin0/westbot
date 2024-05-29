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

    if response.status_code == 200:
        return response.json()

    return False


def getCategorys():
    url = f"{BASE_URL}/foods/category/"
    return requests.get(url).json()

def getFoods(category):
    url = f"{BASE_URL}/foods/category/{category}/"

    return requests.get(url).json()

def addBasket(user_id, food_name, count):
    url = BASE_URL + f"/busket/create"
    response = requests.post(url, data={
        'user_id': user_id,
        'food_name':food_name,
        'count':count
        })
    return response.json()


def getFood(food_name):
    url = f"{BASE_URL}/foods/{food_name}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()

    return False


def getBasketList(user_id):
    url = BASE_URL + f"/busket/list?user_id={user_id}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False


def getBasketItem(basket_id):
    response = requests.get(BASE_URL + f"food/busket-item?basket_id={basket_id}")
    return response.json()


def changeBasketItem(basket_id, action):
    response = requests.get(BASE_URL + f'/food/busket-change?basket_id={basket_id}&action={action}')
    return response.json()

def clearBasketAndSetRating(user_id):
    
    response = requests.get(BASE_URL + f'/busket/clear-and-rating?user_id={user_id}')
    return response.json()

def deleteBasket(food_name, user_id):
    response = requests.get(BASE_URL + f'/busket/delete?food_name={food_name}&user_id={user_id}')
    return response.json()
