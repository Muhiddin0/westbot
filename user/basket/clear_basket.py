from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from services.services import clearBasketAndSetRating, getUser

from user.orderd.start_order import order
from utils import buttons, texts

from states import FoodOrder

async def _task(message: types.Message, state: FSMContext):
    """
    """ 

    # user id
    user_id = message.from_user.id
    
    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']
    
    clearBasketAndSetRating(user_id)

    await message.answer(texts.CLEAR_BASKET[lang])
    await order(message, state)

@dp.message_handler(
    lambda message: message.text.startswith("🆑"),
    state="*")
async def user_basket_clear(message: types.Message, state: FSMContext):
    create_task(_task(message, state))