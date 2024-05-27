from aiogram.types import Message
from asyncio import create_task
from aiogram.dispatcher import FSMContext

from bot.loader import dp
from bot.utils import buttons, texts





async def contact(message: Message, state: FSMContext):


    await message.answer(texts.CONTACT_UZ, reply_markup=buttons.REMOVE_BUTTON)



@dp.message_handler(
    lambda message: message.text.startswith(buttons.MENU_CONTACT_UZ) or \
                    message.text.startswith(buttons.MENU_BUTTONS_RU) or \
                    message.text.startswith(buttons.MENU_BUTTONS_EN)
)
async def func(message: Message, state: FSMContext):
    await create_task(contact(message, state))