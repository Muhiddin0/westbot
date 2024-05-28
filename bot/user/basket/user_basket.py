
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from services.services import getBasketList
from states import Register

from tempuser import USER

from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    """ 

    # user id
    user_id = message.from_user.id
    user_basket = getBasketList(user_id)

    print(user_basket)


@dp.message_handler(
    lambda message: message.text.startswith((
                        buttons.BASKET_UZ,)
                        ),
    state='*')
async def user_basket(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
