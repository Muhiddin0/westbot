from aiogram.dispatcher.storage import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.loader import dp
from asyncio import create_task
from asgiref.sync import sync_to_async
from aiogram.types import CallbackQuery
from backend.bot.models import UserPhones, User
# from ..registrations import phone
from bot.states import Delivery
from ...services.services import getUser
from ...utils import texts, buttons


async def delivery_task(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']
    print(lang)

    # menu yuborish
    await message.answer(text=texts.MENU[lang], reply_markup=buttons.MENU[lang])

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
        user_phone = await sync_to_async(UserPhones.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    phone_list_user_uz = ReplyKeyboardMarkup(
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
    phone_list_user_en = ReplyKeyboardMarkup(
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
    phone_list_user_ru = ReplyKeyboardMarkup(
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

    PHONE_LIST = {
        'uz': phone_list_user_uz,
        'ru': phone_list_user_ru,
        'en': phone_list_user_en,
    }

    await message.answer(texts.PHONE[lang], reply_markup=PHONE_LIST[lang])

    await state.set_state(Delivery.phone)

@dp.message_handler(text='🚚 Yetkazib berish', content_types=['text'])
async def change_basket(message: Message, state: FSMContext):
    create_task(delivery_task(message, state))

