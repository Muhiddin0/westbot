
from asyncio import create_task
from aiogram import types
from aiogram.dispatcher import FSMContext

from services.services import getUser
from states import Register

from tempuser import USER

from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    Ro'yxatdan o'tgan userlar uchun asosiy menu
    """ 

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    
    # menu yuborish
    await message.answer(text=texts.MENU[lang], reply_markup=buttons.MENU[lang])
    
    # bundan oldinga barcha statlarni o'chirish
    await state.finish()

    
async def MainMenu(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
