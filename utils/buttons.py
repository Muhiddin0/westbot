from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton,\
                            ReplyKeyboardRemove


REMOVE_BUTTON = ReplyKeyboardRemove()

from utils.functions import calc_delivered_time

BACK_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            '⬅️ Ortga'
        ],
    ],
    resize_keyboard=True
)

BACK_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            '⬅️ Назад'
        ],
    ],
    resize_keyboard=True
)

BACK_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            '⬅️ BACK'
        ],
    ],
    resize_keyboard=True
)


BACK = {
    'uz': BACK_UZ,
    'ru': BACK_RU,
    'en': BACK_EN,
}


MENU_ORDER_UZ = '🛍 Buyurtma berish'
MENU_FEEDBACK_UZ = '✍️ Fikr bildirish'
MENU_CONTACT_UZ = '☎️ Biz bilan aloqa'
MENU_INFO_UZ = "ℹ️ Ma'lumot"
MENU_SETTINGS_UZ = "⚙️ Sozlamalar"

MENU_ORDER_RU = '🛍 Заказать'
MENU_FEEDBACK_RU = '✍️ Комментарий'
MENU_CONTACT_RU = '☎️ Связаться с нами'
MENU_INFO_RU = "ℹ️ Информация"
MENU_SETTINGS_RU = "⚙️ Настройки"

MENU_ORDER_EN = '🛍 Order'
MENU_FEEDBACK_EN = '✍️ Comment'
MENU_CONTACT_EN = '☎️ Contact us'
MENU_INFO_EN = "ℹ️ Reference"
MENU_SETTINGS_EN = "⚙️ Settings"

LANGUAGES_UZ = "🇺🇿 O'zbekcha"
LANGUAGES_RU = "🇷🇺 Русский"
LANGUAGES_EN = "🏴󠁧󠁢󠁥󠁮󠁧󠁿 English"

MENU_BUTTONS_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [MENU_ORDER_UZ],
        [MENU_FEEDBACK_UZ, MENU_CONTACT_UZ],
        [MENU_INFO_UZ, MENU_SETTINGS_UZ]
    ],
    resize_keyboard=True
)

MENU_BUTTONS_RU = ReplyKeyboardMarkup(
    keyboard=[
        [MENU_ORDER_RU],
        [MENU_FEEDBACK_RU, MENU_CONTACT_RU],
        [MENU_INFO_RU, MENU_SETTINGS_RU]
    ],
    resize_keyboard=True
)


MENU_BUTTONS_EN = ReplyKeyboardMarkup(
    keyboard=[
        [MENU_ORDER_EN],
        [MENU_FEEDBACK_EN, MENU_CONTACT_EN],
        [MENU_INFO_EN, MENU_SETTINGS_EN]
    ],
    resize_keyboard=True
)


MENU = {
    'uz': MENU_BUTTONS_UZ,
    'ru': MENU_BUTTONS_RU,
    'en': MENU_BUTTONS_EN,
}

LANGUAGES = ReplyKeyboardMarkup(
    keyboard=[
        [LANGUAGES_UZ],
        [LANGUAGES_RU],
        [LANGUAGES_EN],
    ],
    resize_keyboard=True,
)


PHONE_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Raqamni jo'natish", request_contact=True)
        ],
    ],
    resize_keyboard=True,
)

PHONE_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Отправка номера", request_contact=True)
        ],
    ],
    resize_keyboard=True,
)

PHONE_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Send number", request_contact=True)
        ],
    ],
    resize_keyboard=True,
)
PHONE = {
    'uz': PHONE_UZ,
    'ru': PHONE_RU,
    'en': PHONE_EN,
}


COMMENT_STATUS_ONE_UZ = 'Hammasi yoqdi ♥️'
COMMENT_STATUS_TWO_UZ = 'Yaxshi ⭐️⭐️⭐️⭐️'
COMMENT_STATUS_THERE_UZ = 'Yoqmadi ⭐️⭐️⭐️'
COMMENT_STATUS_FOUR_UZ = "Yomon ⭐️⭐️"
COMMENT_STATUS_FIVE_UZ = 'Juda yomon 👎🏻'
COMMENT_BACK_UZ = '⬅️ Ortga'

COMMENT_STATUS_ONE_RU = 'Мне все понравилось ♥️'
COMMENT_STATUS_TWO_RU = 'Хорошо ⭐️⭐️⭐️⭐️'
COMMENT_STATUS_THERE_RU = 'Не понравилось ⭐️⭐️⭐️'
COMMENT_STATUS_FOUR_RU = "Плохо ⭐️⭐️"
COMMENT_STATUS_FIVE_RU = 'Очень плохо 👎🏻'
COMMENT_BACK_RU = '⬅️ Назад'

COMMENT_STATUS_ONE_EN = 'I liked it all ♥️'
COMMENT_STATUS_TWO_EN = 'Good ⭐️⭐️⭐️⭐️'
COMMENT_STATUS_THERE_EN = 'Did not like ⭐️⭐️⭐️'
COMMENT_STATUS_FOUR_EN = "Bad ⭐️⭐️"
COMMENT_STATUS_FIVE_EN = 'Too bad 👎🏻'
COMMENT_BACK_EN = '⬅️ back'


COMMENT_STATUS_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            COMMENT_STATUS_ONE_UZ,
        ],
        [
            COMMENT_STATUS_TWO_UZ,
        ],
        [
            COMMENT_STATUS_THERE_UZ,
        ],
        [
            COMMENT_STATUS_FOUR_UZ,
        ],
        [
            COMMENT_STATUS_FIVE_UZ,
        ],
        [
            COMMENT_BACK_UZ,
        ],
    ],
    resize_keyboard=True
)

COMMENT_STATUS_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            COMMENT_STATUS_ONE_RU,
        ],
        [
            COMMENT_STATUS_TWO_RU,
        ],
        [
            COMMENT_STATUS_THERE_RU,
        ],
        [
            COMMENT_STATUS_FOUR_RU,
        ],
        [
            COMMENT_STATUS_FIVE_RU,
        ],
        [
            COMMENT_BACK_RU,
        ],
    ],
    resize_keyboard=True
)


COMMENT_STATUS_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            COMMENT_STATUS_ONE_EN,
        ],
        [
            COMMENT_STATUS_TWO_EN,
        ],
        [
            COMMENT_STATUS_THERE_EN,
        ],
        [
            COMMENT_STATUS_FOUR_EN,
        ],
        [
            COMMENT_STATUS_FIVE_EN,
        ],
        [
            COMMENT_BACK_EN,
        ],
    ],
    resize_keyboard=True
)



TIL_SOZLAMALARI_BUTTON_UZ = "🔄 Tilni o'zgartirish"
TIL_SOZLAMALARI_BUTTON_EN = "🔄 Change language"
TIL_SOZLAMALARI_BUTTON_RU = "🔄 Смена языка"

PHONE_SWITCH_UZ = "📞 Telefon raqamni o'zgartirish"
PHONE_SWITCH_EN = "📞 Change phone number"
PHONE_SWITCH_RU = "📞 Смена номера телефона"

FULLNAME_SWITCH_UZ = "Ismni o'zgartirish"
FULLNAME_SWITCH_RU = "Изменение имени"
FULLNAME_SWITCH_EN = "Name change"


ORTGA_BUTTON_UZ = "🔙 Ortga"
ORTGA_BUTTON_EN = "🔙 Back"
ORTGA_BUTTON_RU = "🔙 Назад"

ORTGA = {
    'uz': ReplyKeyboardMarkup(
        keyboard=[
            [ORTGA_BUTTON_UZ]
        ],
        resize_keyboard=True
    ),
    'ru': ReplyKeyboardMarkup(
        keyboard=[
            [ORTGA_BUTTON_RU]
        ],
        resize_keyboard=True
    ),
    'en': ReplyKeyboardMarkup(
        keyboard=[
            [ORTGA_BUTTON_EN]
        ],
        resize_keyboard=True
    ),
}

SETTINGS_MENYU_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            FULLNAME_SWITCH_UZ,
            TIL_SOZLAMALARI_BUTTON_UZ
        ],
        [
            PHONE_SWITCH_UZ
        ],
        [
            ORTGA_BUTTON_UZ
        ],
    ],
    resize_keyboard=True
)

SETTINGS_MENYU_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            FULLNAME_SWITCH_RU,
            TIL_SOZLAMALARI_BUTTON_RU
        ],
        [
            PHONE_SWITCH_RU
        ],
        [
            ORTGA_BUTTON_RU
        ],
    ],
    resize_keyboard=True
)

SETTINGS_MENYU_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            FULLNAME_SWITCH_EN,
            TIL_SOZLAMALARI_BUTTON_EN
        ],
        [
            PHONE_SWITCH_EN
        ],
        [
            ORTGA_BUTTON_EN
        ],
    ],
    resize_keyboard=True
)


SETTINGS_MENYU = {
    'uz': SETTINGS_MENYU_UZ,
    'ru': SETTINGS_MENYU_RU,
    'en': SETTINGS_MENYU_EN,

}

INFO_LOCATION_UZ = "🕹 Manzilni ko'rish"
INFO_LOCATION_EN = "🕹 View address"
INFO_LOCATION_RU = "🕹 Просмотр адреса"


INFORMATION_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=INFO_LOCATION_UZ),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_UZ),
        ]
    ],
    resize_keyboard=True
)

INFORMATION_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=INFO_LOCATION_RU),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_RU),
        ]
    ],
    resize_keyboard=True
)


INFORMATION_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=INFO_LOCATION_EN),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_EN),
        ]
    ],
    resize_keyboard=True
)

INFORMATION = {
    'uz': INFORMATION_UZ,
    'ru': INFORMATION_RU,
    'en': INFORMATION_EN,

}



CLEAR_BASKET_UZ = "🆑 Savatni tozalash"
BASKET_UZ = "🛒 Savat"
DELIVER_UZ = "🚚 Yetkazib berish"
TAKE_UZ = '🏃🏻‍♂️ Olib ketish'

CLEAR_BASKET_RU = "🆑 Очистить корзину"
BASKET_RU = "🛒 Корзина"
DELIVER_RU = "🚚 Доставка"
TAKE_RU = '🏃🏻‍♂️ Самовывоз'

CLEAR_BASKET_EN = "🆑 Clear Basket"
BASKET_EN = "🛒 Basket"
DELIVER_EN = "🚚 Delivery"
TAKE_EN = '🏃🏻‍♂️ Pickup'

def USER_BASKET(user_basket, lang):
    food_buttons = []
    for i in user_basket:
        food_buttons.append([KeyboardButton(text="❌ " + i['food']['name_' + lang])])

    if lang == 'uz':
        return ReplyKeyboardMarkup(
            keyboard= food_buttons + [
                [
                    ORTGA_BUTTON_UZ,
                    CLEAR_BASKET_UZ
                ],
                [DELIVER_UZ]
            ],
            resize_keyboard=True
        )
    elif lang == 'ru':
        return ReplyKeyboardMarkup(
            keyboard= food_buttons + [
                [
                    ORTGA_BUTTON_RU,
                    CLEAR_BASKET_RU
                ],
                [DELIVER_RU]
            ],
            resize_keyboard=True
        )
    else:
        return ReplyKeyboardMarkup(
            keyboard= food_buttons + [
                [
                    ORTGA_BUTTON_EN,
                    CLEAR_BASKET_EN
                ],
                [DELIVER_EN]
            ],
            resize_keyboard=True
        )

def ORDER_BUTTONS(category, lang):
    category_buttons = []

    for i in category:
        # Initialize a new row if the last row is filled or if it's the first button
        if len(category_buttons) == 0 or len(category_buttons[-1]) == 2:
            category_buttons.append([])

        category_name = 'name_' + lang
        # Append the category name button to the last row
        category_buttons[-1].append(KeyboardButton(i[category_name]))
    
    if lang == 'uz':
        button = ReplyKeyboardMarkup(
            row_width=2,
            keyboard=[
                [BASKET_UZ],
                [DELIVER_UZ, TAKE_UZ],
            ],
            resize_keyboard=True
        )
        
        # Adding the category buttons to the main keyboard
        for row in category_buttons:
            button.keyboard.append(row)

        button.add(ORTGA_BUTTON_UZ)
        return button
        
    elif lang == 'ru':
        button = ReplyKeyboardMarkup(
            row_width=2,
            keyboard=[
                [BASKET_RU],
                [DELIVER_RU, TAKE_RU],
            ],
            resize_keyboard=True
        )
        
        # Adding the category buttons to the main keyboard
        for row in category_buttons:
            button.keyboard.append(row)

        button.add(ORTGA_BUTTON_RU)
        return button

    else:
        button = ReplyKeyboardMarkup(
            row_width=2,
            keyboard=[
                [BASKET_RU],
                [DELIVER_RU, TAKE_RU],
            ],
            resize_keyboard=True
        )
        
        # Adding the category buttons to the main keyboard
        for row in category_buttons:
            button.keyboard.append(row)

        button.add(ORTGA_BUTTON_EN)
        return button


def FOODS_BUTTONS(foods, lang):
    food_buttons = []
    for i in foods:
        # Initialize a new row if the last row is filled or if it's the first button
        if len(food_buttons) == 0 or len(food_buttons[-1]) == 2:
            food_buttons.append([])

        # Append the category name button to the last row
        food_buttons[-1].append(KeyboardButton(i['name_uz']))
    
    if lang == 'uz':
        # Initialize the ReplyKeyboardMarkup with initial buttons
        button = ReplyKeyboardMarkup(
            row_width=2,
            keyboard=[
                [BASKET_UZ, DELIVER_UZ],
            ],
            resize_keyboard=True
        )
        
        # Adding the category buttons to the main keyboard
        for row in food_buttons:
            button.keyboard.append(row)

        button.add(ORTGA_BUTTON_UZ)
        return button

    elif lang == 'ru':
        # Initialize the ReplyKeyboardMarkup with initial buttons
        button = ReplyKeyboardMarkup(
            row_width=2,
            keyboard=[
                [BASKET_RU, DELIVER_RU],
            ],
            resize_keyboard=True
        )
        
        # Adding the category buttons to the main keyboard
        for row in food_buttons:
            button.keyboard.append(row)

        button.add(ORTGA_BUTTON_UZ)
        return button
    else:
        # Initialize the ReplyKeyboardMarkup with initial buttons
        button = ReplyKeyboardMarkup(
            row_width=2,
            keyboard=[
                [BASKET_RU, DELIVER_RU],
            ],
            resize_keyboard=True
        )
        
        # Adding the category buttons to the main keyboard
        for row in food_buttons:
            button.keyboard.append(row)

        button.add(ORTGA_BUTTON_UZ)
        return button


LOCATION_UZ = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Manzilni yuborish", request_location=True)
            ]
        ],
        resize_keyboard=True
    )

LOCATION_EN = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Send address", request_location=True)
            ]
        ],
        resize_keyboard=True
    )

LOCATION_RU = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Отправить адрес", request_location=True)
            ]
        ],
        resize_keyboard=True
    )


RETURN_MAIN_MENYU_UZ = '🏡 Bosh menyuga qaytish'
RETURN_MAIN_MENYU_RU = '🏡 Bosh menyuga qaytish'
RETURN_MAIN_MENYU_EN = '🏡 Bosh menyuga qaytish'


FOOD_RETRIVE_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ],
        [
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
        ], 
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_UZ),
            KeyboardButton(text=RETURN_MAIN_MENYU_UZ),
        ]
    ],
    resize_keyboard=True
)


FOOD_RETRIVE_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ],
        [
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
        ], 
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_UZ),
            KeyboardButton(text=RETURN_MAIN_MENYU_UZ),
        ]
    ],
    resize_keyboard=True
)


FOOD_RETRIVE_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ],
        [
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
        ], 
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_UZ),
            KeyboardButton(text=RETURN_MAIN_MENYU_UZ),
        ]
    ],
    resize_keyboard=True
)




FOOD_RETRIVE = {
    'uz': FOOD_RETRIVE_UZ,
    'ru': FOOD_RETRIVE_RU,
    'en': FOOD_RETRIVE_EN,
}


def NEW_DELIVERY(user_id, distance, link):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"y_new_d:-user_id:{user_id}-dis:{distance}")],
        [InlineKeyboardButton("❌ Rad etish", callback_data=f"n_new_d:-user_id:{user_id}")],
        [InlineKeyboardButton("🏘  Xaritadan ko'rish", url=link)],
    ])
    
    
    

# MAIN MENU UZ BUTTONS
BUYURTMA_BUTTON_UZ = '📦 Buyurtma berish'
FIKR_BUTTON_UZ = '✍️ Fikr bildirish'
BUYURTMALARIM_BUTTON_UZ = '📝 Mening Buyurmalarim'
SOZLAMALAR_BUTTON_UZ = '⚙️ Sozlamalar'
SHARTLAR_BUTTON_UZ = "ℹ️ Ma'lumot"

# MAIN MENU CR BUTTONS
BUYURTMA_BUTTON_EN = '📦 Order'  # Заказать
FIKR_BUTTON_EN = '✍️ Feedback'  # Предложить идею
BUYURTMALARIM_BUTTON_EN = '📝 My Orders'  # Мои заказы
SOZLAMALAR_BUTTON_EN = '⚙️ Settings'  # Настройки
SHARTLAR_BUTTON_EN = "ℹ️ Reference"  # Условия использования




# MAIN MENU RU BUTTONS
BUYURTMA_BUTTON_RU = '📦 Заказать'  
FIKR_BUTTON_RU = '✍️ Предложить идею'  
BUYURTMALARIM_BUTTON_RU = '📝 Мои Заказы'  
SOZLAMALAR_BUTTON_RU = '⚙️ Настройки'  
SHARTLAR_BUTTON_RU = "ℹ️ информация"

def PREPARING(user_id, dis, maps_link):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✈️ Jo'natish", callback_data=f"preparing:-user_id:{user_id}-dis:{dis}")],
        [InlineKeyboardButton("🏘  Xaritadan ko'rish", url=maps_link)]
    ])

def DELIVER_SPEED(user_id, dis, maps_link):
    del_speed_3 = calc_delivered_time(dis, 3)
    del_speed_7 = calc_delivered_time(dis, 7)
    del_speed_20 = calc_delivered_time(dis, 20)
    del_speed_45 = calc_delivered_time(dis, 45)
    
    # send_deliver:-user_id:{}-del_time
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(f"🏃‍♂️ 1km/s - 5 km/s = {del_speed_3}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_3}")],
        [InlineKeyboardButton(f"🚴 5km/s - 10 km/s = {del_speed_7}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_7}")],
        [InlineKeyboardButton(f"🛵 10km/s - 30 km/s = {del_speed_20}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_20}")],
        [InlineKeyboardButton(f"🚚 30km/s - 60 km/s = {del_speed_45}", callback_data=f"s_deliver:-user_id:{user_id}-del_time:{del_speed_3}")],
        [InlineKeyboardButton("🏘  Xaritadan ko'rish", url=maps_link)]
    ])


def REMOVE_TAKE(message_id, user_id):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("🗑 Olib tashlash", callback_data=f"trash_take:{message_id}-user_id:{user_id}")]
    ])


def REMOVE_COMMENT(message_id, user_id):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("🗑 Olib tashlash", callback_data=f"trash_comment:{message_id}-user_id:{user_id}")]
    ])

def NEW_DELIVERY(user_id, distance, link):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"y_new_d:-user_id:{user_id}-dis:{distance}")],
        [InlineKeyboardButton("❌ Rad etish", callback_data=f"n_new_d:-user_id:{user_id}")],
        [InlineKeyboardButton("🏘  Xaritadan ko'rish", url=link)],
    ])


def NEW_TAKE(user_id):
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"t_succes:-user_id:{user_id}")],
        [InlineKeyboardButton("❌ Rad etish", callback_data=f"n_new_d:-user_id:{user_id}")]
    ])

def DECLINE_DELIVERY_STATUS(user_id, lang='uz'): 
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton("Maxsulot qolmadi", callback_data=f"decline_status:empty_food-user_id:{user_id}-lang:{lang}")],
    [InlineKeyboardButton("Kurier yetishmasligi", callback_data=f"decline_status:empty_kurier-user_id:{user_id}-lang:{lang}")],
    [InlineKeyboardButton("Nomalum xatolik", callback_data=f"decline_status:other-user_id:{user_id}-lang:{lang}")],
])

def DELIVER_ERROR_BUTTONS(maps_link, user_id): 
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                [InlineKeyboardButton("Yetkazib berildi", callback_data=f"succes:-user_id:{user_id}")],
                [InlineKeyboardButton("SHikastlangan holda yetib bordi", callback_data=f"damaget:-user_id:{user_id}")],
                [InlineKeyboardButton("Maxsulot qolmadi", callback_data=f"not_product:-user_id:{user_id}")],
                [InlineKeyboardButton("Noma'lum xatolik yuz berdi", callback_data=f"unknown:-user_id:{user_id}")],
                [InlineKeyboardButton("🏘  Xaritadan ko'rish", url=maps_link)]
])


def DELIVERY_PREPARING_BUTTON(distance, user_id): 
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                [InlineKeyboardButton("🧑‍🍳 Buyurtma tayyorlanmoqda..", callback_data=f"d_preparing:-user_id:{user_id}-dis:{distance}")],
])


def TAKE_PREPARING_BUTTON(user_id): 
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                [InlineKeyboardButton("🧑‍🍳 Buyurtma tayyorlanmoqda..", callback_data=f"t_preparing:-user_id:{user_id}")],
])


def TAKE_READY_BUTTON(user_id): 
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                [InlineKeyboardButton("🍲 Buyurtma tayyor", callback_data=f"t_ready:-user_id:{user_id}")],
])






def MAIN_MENU(lang='uz'):
    if lang == 'uz':
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    BUYURTMA_BUTTON_UZ
                ],
                [
                    FIKR_BUTTON_UZ,
                    BUYURTMALARIM_BUTTON_UZ
                ],
                [
                    SOZLAMALAR_BUTTON_UZ,
                    SHARTLAR_BUTTON_UZ
                ],
            ],
            resize_keyboard=True
        )
    
    if lang == 'en':
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    BUYURTMA_BUTTON_EN
                ],
                [
                    FIKR_BUTTON_EN,
                    BUYURTMALARIM_BUTTON_EN
                ],
                [
                    SOZLAMALAR_BUTTON_EN,
                    SHARTLAR_BUTTON_EN
                ],
            ],
            resize_keyboard=True
        )
    
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                BUYURTMA_BUTTON_RU
            ],
            [
                FIKR_BUTTON_RU,
                BUYURTMALARIM_BUTTON_RU
            ],
            [
                SOZLAMALAR_BUTTON_RU,
                SHARTLAR_BUTTON_RU
            ],
        ],
        resize_keyboard=True
    )

def GET_CATEGORY(lang='uz'):
    if lang == 'uz':
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🍽 Buyurtma berish", callback_data="category_redirect:"),
            ]
        ])
    elif lang == 'en':
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🍽 Order", callback_data="category_redirect:"),
            ]
        ])
    else:
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🍽 Заказать", callback_data="category_redirect:"),
            ]
        ])


def COUNTER_MENU(food_id, category_id, count, lang='ru', subtraction=1):
    calc_buttons = [
        [
            InlineKeyboardButton(text="+1", callback_data=f"food:{food_id}/category:{category_id}/number:1"),
            InlineKeyboardButton(text="+2", callback_data=f"food:{food_id}/category:{category_id}/number:2"),
            InlineKeyboardButton(text="+3", callback_data=f"food:{food_id}/category:{category_id}/number:3"),
        ],
        [
            InlineKeyboardButton(text="-1", callback_data=f"food:{food_id}/category:{category_id}/number:-1"),
            InlineKeyboardButton(text="-2", callback_data=f"food:{food_id}/category:{category_id}/number:-2"),
            InlineKeyboardButton(text="-3", callback_data=f"food:{food_id}/category:{category_id}/number:-3"),
        ][0:subtraction]
    ]
    
    if lang == 'uz':
        calc_buttons.append([
                InlineKeyboardButton(text="⬅️ Orqaga", callback_data="category:" + category_id),
            ])
        calc_buttons.append([
                InlineKeyboardButton(text="🛒 Savatcha qo'shish", callback_data=f"basket:start-food:{food_id}-category:{category_id}-number:{count}"),
            ])

    elif lang == 'en':
        calc_buttons.append([
                InlineKeyboardButton(text="⬅️ Back", callback_data="category:" + category_id),
            ])
        calc_buttons.append([
                InlineKeyboardButton(text="🛒 Add basket", callback_data=f"basket:start-food:{food_id}-category:{category_id}-number:{count}"),
            ])
    else:
        calc_buttons.append([
                InlineKeyboardButton(text="⬅️ Назад", callback_data="category:" + category_id),
            ])
        calc_buttons.append([
                InlineKeyboardButton(text="🛒 Добавить в корзину", callback_data=f"basket:start-food:{food_id}-category:{category_id}-number:{count}"),
            ])
            
    return InlineKeyboardMarkup(inline_keyboard=calc_buttons)

    
REGISTER_BUTTON = "📝 Ro'yxatdan o'tish"
REGISTER = ReplyKeyboardMarkup(
    keyboard=[
        [
            REGISTER_BUTTON
        ]
    ],
     resize_keyboard=True
)

TIL_SOZLAMALARI_BUTTON_UZ = "🔄 Tilni o'zgartirish"
TIL_SOZLAMALARI_BUTTON_EN = "🔄 Change language"
TIL_SOZLAMALARI_BUTTON_RU = "🔄 Смена языка"

PHONE_SWITCH_UZ = "📞 Telefon raqamni o'zgartirish"
PHONE_SWITCH_EN = "📞 Change phone number"
PHONE_SWITCH_RU = "📞 Смена номера телефона"



SETTINGS_MENYU_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            TIL_SOZLAMALARI_BUTTON_UZ,
        ],
        [
            PHONE_SWITCH_UZ
        ],
        [
            ORTGA_BUTTON_UZ
        ]
    ],
    resize_keyboard=True
)

SETTINGS_MENYU_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            TIL_SOZLAMALARI_BUTTON_EN,
        ],
        [
            PHONE_SWITCH_EN
        ],
        [
            ORTGA_BUTTON_EN
        ]
    ],
    resize_keyboard=True
)

SETTINGS_MENYU_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            TIL_SOZLAMALARI_BUTTON_RU,
        ],
        [
            PHONE_SWITCH_RU
        ],
        [
            ORTGA_BUTTON_RU
        ]
    ],
    resize_keyboard=True
)

ORTGA_MAIN_BUTTON_UZ = '🔙 Ortga'
ORTGA_MAIN_BUTTON_EN = '🔙 Back'
ORTGA_MAIN_BUTTON_RU = '🔙 Назад'




BACK_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            ORTGA_MAIN_BUTTON_UZ
        ],
    ],
    resize_keyboard=True,
)

BACK_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            ORTGA_MAIN_BUTTON_EN
        ],
    ],
    resize_keyboard=True,
)

BACK_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            ORTGA_MAIN_BUTTON_RU
        ],
    ],
    resize_keyboard=True,
)

HA_BUTTON_UZ = "✅ Ha"
YOQ_BUTTON_UZ = "❌ Yoq"

HA_BUTTON_EN = "✅ Yes"
YOQ_BUTTON_EN = "❌ No"

HA_BUTTON_RU = "✅ Ha"
YOQ_BUTTON_RU = "❌ нет"


REFFERAL_REQUEST_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            HA_BUTTON_UZ,
            YOQ_BUTTON_UZ
        ],
        [
            ORTGA_BUTTON_UZ
        ]
    ],
    resize_keyboard=True,
)

REFFERAL_REQUEST_EN = ReplyKeyboardMarkup(
    keyboard=[
        [
            HA_BUTTON_EN,
            YOQ_BUTTON_EN
        ],
        [
            ORTGA_BUTTON_EN
        ]
    ],
    resize_keyboard=True,
)

REFFERAL_REQUEST_RU = ReplyKeyboardMarkup(
    keyboard=[
        [
            HA_BUTTON_RU,
            YOQ_BUTTON_RU
        ],
        [
            ORTGA_BUTTON_RU
        ]
    ],
    resize_keyboard=True,
)

# CONTACT_BUTTON = KeyboardButton(text="Запросить контакт", request_contact=True)
# CONTACT = ReplyKeyboardMarkup(resize_keyboard=True).add(CONTACT_BUTTON)

CONTACT = {
    "uz": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Jo'natish", request_contact=True)
            ]
        ],
        resize_keyboard=True
    ),
    "en": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Send", request_contact=True)
            ]
        ],
        resize_keyboard=True
    ),
    "ru": ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Отправить", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )
}

def SUCCES_BASKET(lang='uz'):
    if (lang=='uz'):
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🛒 Savatchaga o'tish", callback_data="get_backet:")
            ],
            [
                InlineKeyboardButton(text="🍟 Haridni davom etish", callback_data="category_redirect:")
            ]
        ])

    if (lang=='en'):
        return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [
                InlineKeyboardButton(text="🛒 Switch to basket", callback_data="get_backet:")
            ],
            [
                InlineKeyboardButton(text="🍟 Continuing the Harid", callback_data="category_redirect:")
            ]
        ])
        
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Перейти в корзину", callback_data="get_backet:")
        ],
        [
            InlineKeyboardButton(text="🍟 Продолжение покупки", callback_data="category_redirect:")
        ]
    ])

LOCATION_UZ = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Manzilni yuborish", request_location=True)
            ]
        ],
        resize_keyboard=True
    )

LOCATION_EN = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Send address", request_location=True)
            ]
        ],
        resize_keyboard=True
    )

LOCATION_RU = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🕹 Отправить адрес", request_location=True)
            ]
        ],
        resize_keyboard=True
    )



TAKE_PHONE_UZ = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Jo'natish", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

TAKE_PHONE_EN = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Send", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

TAKE_PHONE_RU = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📞 Отправить", request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

def CATEGORY_BUTTONS(lang='uz', category=None):
    categoey_buttons_array = []
    if (lang == "uz"):
        for i in category:
            categoey_buttons_array.append(
                InlineKeyboardButton(text=i.name_uz, callback_data="category:" + str(i.id)),
            )
    elif (lang == "en"):
        for i in category:
            categoey_buttons_array.append(
                InlineKeyboardButton(text=i.name_cr, callback_data="category:" + str(i.id)),
            )
    else:
        for i in category:
            categoey_buttons_array.append(
                InlineKeyboardButton(text=i.name_ru, callback_data="category:" + str(i.id)),
            )
            
    categoey_buttons = InlineKeyboardMarkup(row_width=2)
    categoey_buttons.add(*categoey_buttons_array)
            
    return categoey_buttons




def FOODS(lang='uz', foods=None, category_id=None):
    foods_buttons_list = []
    
    if lang == "uz":
        for i in foods:
            foods_buttons_list.append(
                InlineKeyboardButton(text=i.name_uz, callback_data=f"food:{i.id}/category:{category_id}/number:1"),
            )
    elif lang == "en":
        for i in foods:
            foods_buttons_list.append(
                InlineKeyboardButton(text=i.name_en, callback_data=f"food:{i.id}/category:{category_id}/number:1"),
            )
    else:
        for i in foods:
            print(f"food:{i.id}/category:{category_id}/number:1")
            foods_buttons_list.append(
                InlineKeyboardButton(text=i.name_ru, callback_data=f"food:{i.id}/category:{category_id}/number:1"),
            )
    
    foods_buttons = InlineKeyboardMarkup(row_width=2)
    foods_buttons.add(*foods_buttons_list)
    foods_buttons.add(
        InlineKeyboardButton(text="⬅️ Orqaga", callback_data="category_redirect:"),
    )

    return foods_buttons


INFO_LOCATION_UZ = "🕹 Manzilni ko'rish"
INFO_LOCATION_EN = "🕹 View address"
INFO_LOCATION_RU = "🕹 Просмотр адреса"




information_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=INFO_LOCATION_UZ),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_UZ),
        ]
    ],
    resize_keyboard=True
)

information_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=INFO_LOCATION_EN),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_EN),
        ]
    ],
    resize_keyboard=True
)


information_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=INFO_LOCATION_RU),
        ],
        [
            KeyboardButton(text=ORTGA_BUTTON_RU),
        ]
    ],
    resize_keyboard=True
)



INSTAGRAM_BUTTON = InlineKeyboardMarkup(row_width=1)
INSTAGRAM_BUTTON.add(
        InlineKeyboardButton(text="Instagram", callback_data="insta:", url='https://www.instagram.com/west.tashkent/')
    )