from aiogram.types import Message
from asyncio import create_task

from bot.loader import dp
from bot.utils import buttons, texts
from aiogram.dispatcher import FSMContext


async def info_handler(message: Message, state: FSMContext):

    await message.answer(texts.INFO_UZ, reply_markup=buttons.INFORMATION_UZ)


@dp.message_handler(
    lambda message: message.text.startswith(buttons.MENU_INFO_UZ) or \
                    message.text.startswith(buttons.MENU_INFO_RU) or \
                    message.text.startswith(buttons.MENU_INFO_EN)
)
async def func(message: Message, state: FSMContext):
    await create_task(info_handler(message, state))
