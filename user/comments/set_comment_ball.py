from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from asgiref.sync import sync_to_async
from backend.bot.models import User
from utils import buttons
from utils import texts
from states import Comments
from asyncio import create_task



async def set_name_task(message: Message, state: FSMContext):
    ball = message.text
    await state.set_data(
        {
            'ball': ball,
        }
    )
    user_id = message.from_user.id

    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")

    if (lang == "uz"):
        await message.answer(texts.COMMENT_UZ)
    elif (lang == "ru"):
        await message.answer(texts.COMMENT_RU)
    elif (lang == "en"):
        await message.answer(texts.COMMENT_EN)

    await state.set_state(Comments.comment)


@dp.message_handler(content_types=['text'], state=Comments.commen_ball)
async def func(message: Message, state: FSMContext):
    await create_task(set_name_task(message, state))