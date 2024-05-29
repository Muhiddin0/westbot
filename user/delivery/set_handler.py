from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from asyncio import create_task
from aiogram.types import CallbackQuery

from states import Delivery
from services.services import getBasketList, getUser
from utils import texts, buttons


async def delivery_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']

    basket = getBasketList(user_id)

    if not basket:
        await message.answer(text=texts.EMPTY_BASKET[lang])
        return


    # menu yuborish
    await message.answer(text=texts.MENU[lang], reply_markup=buttons.MENU[lang])

    phone_list_user_uz = ReplyKeyboardMarkup(
        keyboard=[
            # [
            #     KeyboardButton(text=phone)
            # ],
            [
                KeyboardButton(text='🔙 Ortga')
            ]
        ],
        resize_keyboard=True
    )
    phone_list_user_en = ReplyKeyboardMarkup(
        keyboard=[
            # [
            #     KeyboardButton(text=phone)
            # ],
            [
                KeyboardButton(text='🔙 Back')
            ]
        ],
        resize_keyboard=True
    )
    phone_list_user_ru = ReplyKeyboardMarkup(
        keyboard=[
            # [
            #     KeyboardButton(text=phone)
            # ],
            [
                KeyboardButton(text='🔙 Назад')
            ]
        ],
        resize_keyboard=True
    )

    PHONE_LIST = {
        'uz': phone_list_user_uz,
        'ru': phone_list_user_ru,
        'en': phone_list_user_en,
    }

    await message.answer(texts.PHONE[lang], reply_markup=PHONE_LIST[lang])

    await state.set_state(Delivery.phone)

@dp.message_handler(
    lambda message: message.text.startswith((
                buttons.DELIVER_UZ,
                buttons.DELIVER_RU,
                buttons.DELIVER_EN,
                )), state="*", content_types=['text'])
async def deliver_food(message: Message, state: FSMContext):
    create_task(delivery_task(message, state))