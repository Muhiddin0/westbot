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

def getFood(food_name):
    url = f"{BASE_URL}/foods/{food_name}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()

    return False


def getBasketList(user_id):
    url = BASE_URL + f"food/busket-list?user_id={user_id}"
    response = requests.get(url)
    return response.json()


def getBasketItem(basket_id):
    response = requests.get(BASE_URL + f"food/busket-item?basket_id={basket_id}")
    return response.json()


def changeBasketItem(basket_id, action):
    response = requests.get(BASE_URL + f'/food/busket-change?basket_id={basket_id}&action={action}')
    return response.json()

def clearBasketAndSetRating(user_id):
    
    response = requests.get(BASE_URL + f'/food/busket-clear-and-rating?user_id={user_id}')
    return response.json()

def deleteBasket(basket_id):
    response = requests.get(BASE_URL + f'/food/basket-delete?basket_id={basket_id}')
    return response.json()



