
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from user.menu import MainMenu
from loader import dp

from services.services import create_user
from states import Register


from utils import buttons, texts
from utils.validators import fullname_validator

async def _task(message: types.Message, state: FSMContext):
    """
    Userni fullnameni olish va ro'yxatdan o'tishni yakunlash
    """

    # userning fullnameini olish
    fullname = message.text

    # fullname ma'lumotlarini tekshirish
    fullname_is_valid = fullname_validator(fullname=fullname)
    
    if not fullname_is_valid:
        # userni tilini olish
        state_data = await state.get_data()
        lang = state_data['lang']
        """
        fullname ma'lumotlari noto'g'ri bo'lsa
        """
        await message.answer(text=texts.FULLNAME_ERROR[lang])
        return

    # userdan fullnameini statega joylash
    await state.update_data({
        'fullname': fullname
    })

    # userni ma'lumotlarini olish
    user = await state.get_data()

    # userni ba'lumotlar bazasiga qo'shish
    create_user(user)

    # userni ro'yxatdan o'tgani haqida habar berish
    await message.answer(text=texts.REGISTER_SUCCESS[user['lang']])

    await MainMenu(message=message, state=state)
    
    # stateni ro'yxatdan o'tishni boshlash
    await state.finish()
    

@dp.message_handler(state=Register.fullname, content_types=types.ContentTypes.TEXT)
async def fullname(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
