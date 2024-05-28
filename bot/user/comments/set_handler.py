from aiogram import types

from ...loader import dp
from ...states import Comments
from asyncio import create_task
from aiogram.dispatcher import FSMContext
from ...utils import buttons, texts
from asgiref.sync import sync_to_async
from backend.bot.models import User


async def comment_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if (user.lang == "uz"):
        await message.answer(texts.COMMENT_BALL_UZ, reply_markup=buttons.COMMENT_STATUS_UZ)
    elif (user.lang == "ru"):
        await message.answer(texts.COMMENT_BALL_RU, reply_markup=buttons.COMMENT_STATUS_RU)
    elif (user.lang == "en"):
        await message.answer(texts.COMMENT_BALL_EN, reply_markup=buttons.COMMENT_STATUS_EN)

    await Comments.commen_ball.set()

@dp.message_handler(
    lambda message: message.text.startswith(buttons.MENU_FEEDBACK_UZ) or \
                    message.text.startswith(buttons.MENU_FEEDBACK_RU) or \
                    message.text.startswith(buttons.MENU_CONTACT_EN)
)
async def func(message: types.Message, state: FSMContext):
    await create_task(comment_handler(message, state))



