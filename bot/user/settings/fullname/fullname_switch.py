from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from backend.bot.models import User
from states import UpdateRegister
from utils import button, texts
from asyncio import create_task
from asgiref.sync import sync_to_async
from loader import dp, bot


async def fullname_switch(message: Message, state: FSMContext):
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    user_id = message.from_user.id
    user = await sync_to_async(User.objects.get)(user_id=user_id)
    lang = user.lang
    state_data = await state.get_data()
    fullname = message.text
    await state.set_data({
        "fullname": fullname
    })
    state_data = await state.get_data()
    fullname = state_data['fullname']
    user.fullname = fullname
    await sync_to_async(user.save)()

    # send contact buttons
    if user.lang == 'uz':
        await message.answer(
            text=texts.FULLNAME_SWITCH[lang],
            reply_markup=button.MENU(lang)
        )
    elif user.lang == 'en':
        await message.answer(
            text=texts.FULLNAME_SWITCH[lang],
            reply_markup=button.MENU(lang)
        )
    elif user.lang == 'ru':
        await message.answer(
            text=texts.FULLNAME_SWITCH[lang],
            reply_markup=button.MENU(lang)
        )

    # finish state
    await state.finish()


@dp.message_handler(state=UpdateRegister.fullname, content_types=['text', 'contact'])
async def phone_number(message: Message, state: FSMContext):
    create_task(fullname_switch(message, state))