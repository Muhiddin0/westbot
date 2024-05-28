
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from services.services import addBasket, getBasketList, getUser

from states import FoodOrder
from utils import buttons, texts

from .order import order

async def _task(message: types.Message, state: FSMContext):
    """
    Bitta maxsulotni ko'rish
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    # xato raqam yuborilsa uni o'chirib tashlash
    count = message.text
    if not count.isdigit():
        await message.delete()
    
    state_data = await state.get_data()
    food_name = state_data['food_name']
    # basketga qo'shish

    # basketga qo'shish
    addBasket(user_id, food_name, count)
    
    await message.answer(texts.SUCCES_ADD[lang])
    
    # categoriyalarni chiqarish
    await order(message, state)

    # stateni tugatish
    await state.finish()
    
    
@dp.message_handler(state=FoodOrder.count)
async def food_quantity(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
    