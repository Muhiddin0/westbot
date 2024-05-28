
from aiogram import types
from aiogram.dispatcher import FSMContext
import requests

from loader import dp

from asyncio import create_task

from services.services import BASE_URL, getFood, getFoods, getUser

from states import FoodOrder
from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    Bitta maxsulotni ko'rish
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    food_name = message.text
    
    # categoryalarni olish
    food = getFood(food_name=food_name)
    
    # tanlang maxsulotni yuborish
    await message.answer_photo(
        photo='https://www.kasandbox.org/programming-images/avatars/leaf-blue.png',
        caption=food['description_uz'],
        reply_markup=buttons.FOOD
        )
    
    
@dp.message_handler(state=FoodOrder.food)
async def order(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
    