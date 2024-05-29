
from aiogram import types
from aiogram.dispatcher import FSMContext
import requests

from loader import dp

from asyncio import create_task

from services.services import getFood, getUser

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
    
    if not food:
        await message.delete()
        return
    
    # tanlang maxsulotni yuborish
    img = requests.get(food['img'])

    if lang == 'uz':
        food_description = food['description_uz']
    elif lang == 'ru':
        food_description = food['description_ru']
    else:
        food_description = food['description_en']
    
    await message.answer_photo(
        photo=img.content,
        caption=texts.FOOD_DESCRIPTION.format(
                food_name,
                food_description
            ),
            reply_markup=buttons.FOOD_RETRIVE[lang],
        )
    
    # user tanlagan maxshulotni statega joylash
    await state.update_data({
        'food_name': food_name
    })
    
    # stateni countga o'tqazish
    await FoodOrder.count.set()
    
    
@dp.message_handler(state=FoodOrder.food)
async def food(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
    