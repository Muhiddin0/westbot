from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from asyncio import create_task
from aiogram.types import CallbackQuery
from services.services import getUser
from states import Delivery
from utils import texts, buttons


async def delivered_task(call: CallbackQuery, state: FSMContext):
    data_split = call.data.split('-')
    user_id = data_split[1].replace("user_id:", "")
    old_message_text = call.message.text
    message_id = call.message.message_id
    
    user = getUser(user_id)
    lang = user['lang']
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.THAKS_SERVICES_DELIVERY[lang]
    )
    
    await call.message.edit_text(
        text=old_message_text + "\n\n" + "✅ Buyurtma tasdiqlandi",
        reply_markup=buttons.REMOVE_TAKE(message_id, user_id)
    )

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("succes:"))
async def delivered(callbask_query: CallbackQuery, state: FSMContext):
    create_task(delivered_task(callbask_query, state))
