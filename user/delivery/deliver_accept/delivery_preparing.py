# from aiogram.dispatcher.storage import FSMContext
# from aiogram.types import CallbackQuery
# from asyncio import create_task
# from services.services import getUser
# from states import Delivery

# from loader import dp, bot


# from utils.constantas import ORDER_SEND_CHAT, ORDER_DELIVERY_MESSAGE_THREAD_ID, KITCHEN_LAN, KITCHEN_LON
# from utils.functions import calculate_distance, create_google_maps_link
# from utils import texts, buttons

# async def delivery_preparing_task(callbask_query: CallbackQuery, state: FSMContext):
#     # user_id = callbask_query.message.from_user.id
#     data_split = callbask_query.data.split('-')
#     user_id = data_split[1].replace("user_id:", "")
    
#     user = getUser(user_id)

#     data = await state.get_data()    
#     phone = data.get('phone')
#     location = data.get('location')

#     if location:
#         user_latitude = location.get('latitude')  # Access latitude attribute
#         user_longitude = location.get('longitude')  # Access longitude attribute

#         zoom_level = 16

#         distance = calculate_distance(
#             user_latitude,
#             user_longitude,
#             KITCHEN_LAN,
#             KITCHEN_LON,
#         )

#         maps_link = create_google_maps_link(user_latitude, user_longitude, zoom_level)

#     # send message curier
#         await bot.send_message(
#             chat_id=ORDER_SEND_CHAT,
#             text=texts.NEW_DELIVERY(
#                 distance=distance,
#                 basket=basket, phone=phone,
#                 maps_link=maps_link
#                 ),
#             reply_to_message_id=ORDER_DELIVERY_MESSAGE_THREAD_ID,
#             reply_markup=buttons.DELIVERY_PREPARING_BUTTON(user_id, distance, maps_link)
#         )
#         # send message succes fuly delivery
#         await callbask_query.message.answer(texts.ORDER_SUCCES_SEND_ADMIN[lang], reply_markup=buttons.MAIN_MENU(lang=lang))
#     else:
#         print("Location data not found.")

# @dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("y_new_d:"))
# @dp.message_handler(state=Delivery.preparing)
# async def y_new_d(callbask_query: CallbackQuery, state: FSMContext):
#     create_task(delivery_preparing_task(callbask_query, state))
