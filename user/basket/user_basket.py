
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from services.services import getBasketList, getUser
from states import FoodOrder

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

    answer_text = "📥 Savat:\n"
    
    for i in user_basket:
        answer_text += f"\n{i['food']['name_uz']}\n"
        answer_text += f"{i['count']} X {i['food']['price']} = {i['count'] * i['food']['price']}\n"
    
    await message.answer(text=answer_text, reply_markup=buttons.USER_BASKET[lang])

    print(user_basket)

@dp.message_handler(
    lambda message: message.text.startswith((
                        buttons.BASKET_UZ,)
                        ),
    state=FoodOrder.category)
async def user_basket(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
