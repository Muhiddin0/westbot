from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery

from asyncio import create_task

from loader import dp, bot
from services.services import clearBasketAndSetRating, getUser

from utils import texts, buttons


async def y_new_d_task(call: CallbackQuery, state: FSMContext):
    # send_deliver:-user_id:{}-delivered_time
    data_split = call.data.split('-')

    user_id = data_split[1].replace("user_id:", "")
    delivered_time = data_split[2].replace("del_time:", "")
    maps_link = call.message.reply_markup.inline_keyboard[-1][0]['url']
    phone_line = call.message.text.split('\n')[-1]

    user = getUser(user_id)
    lang = user['lang']
    
    # Increment rating
    clearBasketAndSetRating(user_id)
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.ACCEPT_DELIVERY[lang].format(delivered_time, phone_line),
    )
    
    await call.message.edit_text(
        text=texts.ORDER_SUCCES_SEND_UZ.format(delivered_time, phone_line),
        reply_markup=buttons.DELIVER_ERROR_BUTTONS(maps_link, user_id)
    )

@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("s_deliver:"))
async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
    create_task(y_new_d_task(callbask_query, state))
