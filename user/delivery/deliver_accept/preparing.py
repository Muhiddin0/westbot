from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from asyncio import create_task
from aiogram.types import CallbackQuery
from services.services import getUser
from utils import texts, buttons


async def y_new_d_task(call: CallbackQuery, state: FSMContext):
    
    data_spelit = call.data.split('-')
    user_id = data_spelit[1].replace("user_id:", "")
    phone_line = call.message.text.split('\n')[-1]
    
    dis = float(data_spelit[2].replace("dis:", ""))
    maps_link = call.message.reply_markup.inline_keyboard[-1][0]['url']

    user = getUser(user_id)
    lang = user['lang']
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.PREPARING_FOOD[lang],
    )
    
    await call.message.edit_text(
        text=texts.PREPARING.format(phone_line),
        reply_markup=buttons.PREPARING(user_id, dis, maps_link)
    )



@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("y_new_d:"))
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    create_task(y_new_d_task(callbask_query, state))
