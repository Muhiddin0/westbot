from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton,\
                            ReplyKeyboardRemove


REMOVE_BUTTON = ReplyKeyboardRemove()

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
