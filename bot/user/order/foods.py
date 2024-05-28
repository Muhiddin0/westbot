
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from services.services import getCategorys, getFoods, getUser

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

    category_name = message.text
    
    # categoryalarni olish
    foods = getFoods(category=category_name)

    if not bool(foods):        
        await message.delete()
        return
    
    await message.answer(text=texts.FOODS[lang], reply_markup=buttons.FOODS_BUTTONS(foods, lang))
    
    await FoodOrder.food.set()
    
@dp.message_handler(state=FoodOrder.category)
async def order(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
