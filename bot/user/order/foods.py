
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from services.services import getCategorys, getFoods, getUser

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
    # foods = getFoods(category=category_name)
    
    # await message.answer(text=texts.FOODS[lang], reply_markup=buttons.FOODS_BUTTONS(foods, lang))
    
    
@dp.message_handler(state='*')
async def order(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
    