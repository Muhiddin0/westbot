
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp

from services.services import deleteBasket

from user.basket.user_basket import user_basket

async def _task(message: types.Message, state: FSMContext):
    """
    """ 

    # user id
    user_id = message.from_user.id
    
    # food name
    food_name = message.text.replace("❌ ", "")
    
    deleteBasket(food_name=food_name, user_id=user_id)

    await user_basket(message, state)

@dp.message_handler(
    lambda message: message.text.startswith("❌"),
    state="*")
async def user_basket_delete(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
