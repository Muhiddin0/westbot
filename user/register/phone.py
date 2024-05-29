
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from states import Register


from utils import texts, buttons

async def _task(message: types.Message, state: FSMContext):
    """
    Userni contact ma'lumotlarini olish va contact ma'lumotin olingandan
    so'ng userni 'fullname' statega o'tqazish
    """

    # userni contact ma'lumotlarini olish
    contact = message.contact.phone_number

    # userni tilini olish
    state_data = await state.get_data()
    lang = state_data['lang']
    
    # userdan fullnameini so'rash
    await message.answer(text=texts.FULLNAME[lang], reply_markup=buttons.REMOVE_BUTTON)
    
    # stateni yangilash, phoneni qo'shish
    await state.set_data({'phone': contact, 'lang': lang})

    # stateni fullnamega o'tqazish
    await Register.fullname.set()

@dp.message_handler(state=Register.phone, content_types=types.ContentTypes.CONTACT)
async def phone(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
