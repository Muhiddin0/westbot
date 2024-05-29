print("1. user_basket...")

from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from services.services import getBasketList, getUser

from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    """ 

    # user id
    user_id = message.from_user.id
    
    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']
    user_basket = getBasketList(user_id)
    
    if not user_basket:
        await message.answer(text=texts.EMPTY_BASKET[lang], reply_markup=buttons.ORTGA[lang])
        return
    
    if lang == 'uz':
        answer_text = "📥 Savat:\n"
        for i in user_basket:
            answer_text += f"\n{i['food']['name_uz']}\n"
            answer_text += f"{i['count']} X {i['food']['price']} = {i['count'] * i['food']['price']}\n"
    elif lang == 'ru':
        answer_text = "📥 Корзина:\n"
        for i in user_basket:
            answer_text += f"\n{i['food']['name_ru']}\n"
            answer_text += f"{i['count']} X {i['food']['price']} = {i['count'] * i['food']['price']}\n"
    elif lang == 'en':
        answer_text = "📥 Basket:\n"
        for i in user_basket:
            answer_text += f"\n{i['food']['name_en']}\n"
            answer_text += f"{i['count']} X {i['food']['price']} = {i['count'] * i['food']['price']}\n"
   
    await message.answer(text=answer_text, reply_markup=buttons.USER_BASKET(user_basket, lang))

    await state.finish()

# @dp.message_handler(
#     text=lambda message: message.text.startswith((
#                         buttons.BASKET_UZ,
#                         buttons.BASKET_RU,
#                         buttons.BASKET_EN,
#                         '🛒 Корзина'
#                         )),
#     state="*"
#     )
@dp.message_handler(state="*", text="🛒 Savat", content_types=types.ContentTypes.TEXT)
async def user_basket(message: types.Message, state: FSMContext):
    create_task(_task(message, state))