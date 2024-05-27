
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from states import Register

from utils import buttons, texts

from tempuser import USER

async def send_welcome_task(message: types.Message, state: FSMContext):
    """
    /start, /help commandalari uchun. Botga birichi kirgan userni anilash
    va uni ro'yxatdan o'rtkazishga jo'natish yoki ro'yxatdan  o'tgan userni
    asosiy menuga o'tqazish 
    """ 

    # user id
    user_id = message.from_user.id

    # user
    user = False  


    if not user:
        """
        Agar user ro'yxatdan o'tmagan bo'lsa
        uni ro'yxatdan o'tqaishga jo'natish
        """
        await message.answer(text=texts.LANGUAGES, reply_markup=buttons.LANGUAGES)
        await Register.lang.set()


@dp.message_handler(state='*', commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    create_task(send_welcome_task(message, state))
