from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from bot.loader import dp, bot
from bot.utils import buttons
from aiogram import Bot
from utils import texts
from asgiref.sync import sync_to_async
from backend.bot.models import User
from bot.states import Comments
from asyncio import create_task




async def set_comment_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        user = await sync_to_async(User.objects.get)(user_id=user_id)
    except:
        raise Exception("User topilmadi")
    if (lang == 'uz'):
        await state.update_data(comment_at=message.text)
        data = await state.get_data()
        ball = data.get('ball')
        add_comment = data.get('comment_at')
        await bot.send_message(
            chat_id='sa',
            text=texts.COMMENT_SEND_UZ(
                ball,
                add_comment,
            ),
        )
    await message.answer(texts.COMMENT_RECEPTION_RU, reply_markup=buttons.COMMENT_BACK_UZ)
    await state.finish()
    if (lang == 'en'):
        await state.update_data(comment_at=message.text)
        data = await state.get_data()
        ball = data.get('ball')
        add_comment = data.get('comment_at')
        await bot.send_message(
            chat_id='sa',
            text=texts.COMMENT_SEND_UZ(
                ball,
                add_comment,
            ),
        )
    await message.answer(texts.COMMENT_RECEPTION_EN, reply_markup=buttons.COMMENT_BACK_UZ)
    await state.finish()

    if (lang == 'ru'):
        await state.update_data(comment_at=message.text)
        data = await state.get_data()
        ball = data.get('ball')
        add_comment = data.get('comment_at')
        await bot.send_message(
            chat_id='sa',
            text=texts.COMMENT_SEND_UZ(
                ball,
                add_comment,
            ),
        )
        await message.answer(texts.COMMENT_RECEPTION_UZ, reply_markup=buttons.COMMENT_BACK_UZ)
        await state.finish()


@dp.message_handler(content_types=['text'], state=Comments.comment)
async def comment(message: Message, state: FSMContext):
    create_task(set_comment_task(message, state))