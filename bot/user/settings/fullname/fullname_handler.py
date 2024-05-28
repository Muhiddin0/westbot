from aiogram.types import Message
from aiogram import Bot
from aiogram.dispatcher import FSMContext
from bot.models import User
from utils import buttons, texts
from asyncio import create_task
from loader import dp, bot
from asgiref.sync import sync_to_async
from states import UpdateRegister
from states import UpdateRegister
from aiogram.types import CallbackQuery
from django.db import transaction


async def lang_switch_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    lang = user.lang
    if (user.lang == 'uz'):
        await message.answer(texts.FULLNAME_SWITCH_SET[lang], parse_mode='HTML', reply_markup=buttons.BACK[lang])
        await state.set_state(UpdateRegister.fullname)
    elif (user.lang == 'en'):
        await message.answer(texts.FULLNAME_SWITCH_SET[lang], parse_mode='HTML', reply_markup=buttons.BACK[lang])
        await state.set_state(UpdateRegister.fullname)

    elif (user.lang == 'ru'):
        await message.answer(texts.FULLNAME_SWITCH_SET[lang], parse_mode='HTML', reply_markup=buttons.BACK[lang])
        await state.set_state(UpdateRegister.fullname)

@dp.message_handler(
        lambda message: message.text.startswith(buttons.FULLNAME_SWITCH_UZ) or \
                message.text.startswith(buttons.FULLNAME_SWITCH_RU) or \
                    message.text.startswith(buttons.FULLNAME_SWITCH_EN)
        )
async def lang_switch(message: Message, state: FSMContext):
    create_task(lang_switch_task(message, state))