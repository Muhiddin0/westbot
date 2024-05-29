from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

# from recyclable.main_menu import main_menu
from utils import texts, buttons
from states import Delivery
from loader import dp

from services.services import getUser


async def set_phone_task(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # user ma'lumotlarin
    user = getUser(user_id)
    lang = user['lang']

    if (lang == "uz"):
        await state.update_data(phone=message.text)
        # phone validator
        if len(message.text) > 8:
            if not ("0" in message.text or
                    "1" in message.text or
                    "2" in message.text or
                    "3" in message.text or
                    "4" in message.text or
                    "5" in message.text or
                    "6" in message.text or
                    "7" in message.text or
                    "8" in message.text or
                    "9" in message.text):
                await message.answer(texts.PHONE_RULE_UZ)
            else:
                await state.set_state(Delivery.location)
                await message.answer(texts.LOCATION_UZ, reply_markup=buttons.LOCATION_UZ)
        else:
            await message.answer(texts.PHONE_NUMBER_LEN_RULE_UZ)
    elif (lang == "en"):
        await state.update_data(phone=message.text)
        if len(message.text) > 8:
            if not ("0" in message.text or
                    "1" in message.text or
                    "2" in message.text or
                    "3" in message.text or
                    "4" in message.text or
                    "5" in message.text or
                    "6" in message.text or
                    "7" in message.text or
                    "8" in message.text or
                    "9" in message.text):
                await message.answer(texts.PHONE_RULE_EN)
            else:
                await state.set_state(Delivery.location)
                await message.answer(texts.LOCATION_EN, reply_markup=buttons.LOCATION_EN)
        else:
            await message.answer(texts.PHONE_NUMBER_LEN_RULE_EN)
    elif (lang == "ru"):
        await state.update_data(phone=message.text)
        # phone validator
        if len(message.text) > 8:
            if not ("0" in message.text or
                    "1" in message.text or
                    "2" in message.text or
                    "3" in message.text or
                    "4" in message.text or
                    "5" in message.text or
                    "6" in message.text or
                    "7" in message.text or
                    "8" in message.text or
                    "9" in message.text):
                await message.answer(texts.PHONE_RULE_RU)
            else:
                await state.set_state(Delivery.location)
                await message.answer(texts.LOCATION_RU, reply_markup=buttons.LOCATION_RU)

        else:
            await message.answer(texts.PHONE_NUMBER_LEN_RULE_RU)


    await state.set_state(Delivery.location)


@dp.message_handler(state=Delivery.phone, content_types=['text'])
async def phone_number(message: types.Message, state: FSMContext):
    create_task(set_phone_task(message, state))
