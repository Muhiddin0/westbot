from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from asyncio import create_task

from bot.services.services import getCategorys, getUser

from bot.utils import buttons, texts
from states import FoodOrder
from utils import buttons, texts

async def _task(message: types.Message, state: FSMContext):
    """
    🛍 Buyurtma berish
    """

    # user id
    user_id = message.from_user.id

    # user ma'lumotlarini olish
    user = getUser(user_id)
    lang = user['lang']

    # categoryalarni olish
    category = getCategorys()

    # categoryani yuborish
    await message.answer(text=texts.ORDER[lang], reply_markup=buttons.ORDER_BUTTONS(category, lang))

    await FoodOrder.category.set()
    
@dp.message_handler(
    lambda message: message.text.startswith((
                        buttons.MENU_ORDER_UZ,)
                        ),
    state='*')
async def order(message: types.Message, state: FSMContext):
    create_task(_task(message, state))
