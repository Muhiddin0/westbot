from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton,\
                            ReplyKeyboardRemove


REMOVE_BUTTON = ReplyKeyboardRemove()
BACK = "⬅️ Ortga"


MENU_ORDER_UZ = '🛍 Buyurtma berish'
MENU_FEEDBACK_UZ = '✍️ Fikr bildirish'
MENU_CONTACT_UZ = '☎️ Biz bilan aloqa'
MENU_INFO_UZ = "ℹ️ Ma'lumot"
MENU_SETTINGS_UZ = "⚙️ Sozlamalar"

MENU_BUTTONS_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [MENU_ORDER_UZ],
        [MENU_FEEDBACK_UZ, MENU_CONTACT_UZ],
        [MENU_INFO_UZ, MENU_SETTINGS_UZ]
    ],
    resize_keyboard=True
)

MENU = {
    'uz':MENU_BUTTONS_UZ
}

LANGUAGES_UZ = "O'zbekcha"
LANGUAGES = ReplyKeyboardMarkup(
    keyboard=[
        [LANGUAGES_UZ],
    ],
    resize_keyboard=True,
)

PHONE_UZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Raqamni jo'natish", request_contact=True)
        ],
    ],
    resize_keyboard=True,
)
PHONE = {
    'uz':PHONE_UZ
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

    button.add(BACK)
        

    return button
