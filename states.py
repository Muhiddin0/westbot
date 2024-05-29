from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    lang = State()
    phone = State()
    fullname = State()
    
class FoodOrder(StatesGroup):
    order = State()
    category = State()
    food = State()
    count = State()

class UpdateRegisterLang(StatesGroup):
    lang = State()

class UpdateRegisterPhone(StatesGroup):
    phone = State()

class UpdateRegisterFullname(StatesGroup):
    fullname = State()

class Comments(StatesGroup):
    commen_ball = State()
    comment = State()
    register_commit = State()

class Delivery(StatesGroup):
    phone = State()
    location = State()
    delivery_send = State()

class TakeAway(StatesGroup):
    phone = State()
    time = State()
