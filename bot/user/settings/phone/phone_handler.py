from aiogram.types import Message
from aiogram import Bot
from aiogram.dispatcher import FSMContext
from bot.models import User, UserPhones
from utils import buttons, texts
from asyncio import create_task
from loader import dp, bot
from asgiref.sync import sync_to_async
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import UpdateRegister
from aiogram.types import CallbackQuery


async def lang_switch_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
        user_phone = await sync_to_async(UserPhones.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    PHONE_LIST_USER_UZ = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=user_phone.phone)
            ],
            [
                KeyboardButton(text='🔙 Ortga')
            ]
        ],
        resize_keyboard=True
    )
    PHONE_LIST_USER_EN = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=user_phone.phone)
            ],
            [
                KeyboardButton(text='🔙 Back')
            ]
        ],
        resize_keyboard=True
    )
    PHONE_LIST_USER_RU = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=user_phone.phone)
            ],
            [
                KeyboardButton(text='🔙 Назад')
            ]
        ],
        resize_keyboard=True
    )

    PHONE_LIST_USER = {
        'uz': PHONE_LIST_USER_UZ,
        'ru': PHONE_LIST_USER_RU,
        'en': PHONE_LIST_USER_EN,
    }
    lang = user.lang
    await message.answer(texts.PHONE_NUMBER_LEN_ERROR[lang], parse_mode='HTML', reply_markup=PHONE_LIST_USER[lang])
    await state.set_state(UpdateRegister.phone)

@dp.message_handler(
        lambda message: message.text.startswith(buttons.PHONE_SWITCH_UZ) or \
                message.text.startswith(buttons.PHONE_SWITCH_EN) or \
                    message.text.startswith(buttons.PHONE_SWITCH_RU)
        )
async def lang_switch(message: Message, state: FSMContext):
    create_task(lang_switch_task(message, state))