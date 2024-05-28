from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton,\
                            ReplyKeyboardRemove


REMOVE_BUTTON = ReplyKeyboardRemove()

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


BASKET_UZ = "🛒 Savat"
DELIVER_UZ = "🚚 Yetkazib berish"


def ORDER_BUTTONS(category, lang):
    # Initialize the ReplyKeyboardMarkup with initial buttons
    button = ReplyKeyboardMarkup(
        row_width=2,
        keyboard=[
            [BASKET_UZ, DELIVER_UZ],
        ],
        resize_keyboard=True
    )
    
    category_buttons = []

    for i in category:
        # Initialize a new row if the last row is filled or if it's the first button
        if len(category_buttons) == 0 or len(category_buttons[-1]) == 2:
            category_buttons.append([])

        category_name = 'name_' + lang
        # Append the category name button to the last row
        category_buttons[-1].append(KeyboardButton(i[category_name]))
    
    # Adding the category buttons to the main keyboard
    for row in category_buttons:
        button.keyboard.append(row)

    button.add(ORTGA_BUTTON_UZ)
    return button


def FOODS_BUTTONS(foods, lang):
    # Initialize the ReplyKeyboardMarkup with initial buttons
    button = ReplyKeyboardMarkup(
        row_width=2,
        keyboard=[
            [BASKET_UZ, DELIVER_UZ],
        ],
        resize_keyboard=True
    )
    
    food_buttons = []

    for i in foods:
        # Initialize a new row if the last row is filled or if it's the first button
        if len(food_buttons) == 0 or len(food_buttons[-1]) == 2:
            food_buttons.append([])

        # Append the category name button to the last row
        food_buttons[-1].append(KeyboardButton(i['name_uz']))
    
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