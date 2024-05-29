from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from services.services import getUser
from states import UpdateRegisterLang
from utils import buttons, texts
from asyncio import create_task
from loader import dp
from asgiref.sync import sync_to_async



async def lang_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)
    
    # olingan til codeni statega joylash
    await state.set_data({
        'lang': lang
    })
    state_data = await state.get_data()
    lang = state_data['lang']
    user.lang = lang
    await sync_to_async(user.save)()
    await message.answer(text=texts.PHONE[lang], reply_markup=buttons.PHONE[lang])

    await state.finish()


@dp.callback_query_handler(state=UpdateRegisterLang.lang)
async def lang(message: Message, state: FSMContext):
    create_task(lang_task(message, state))