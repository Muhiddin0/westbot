from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton,\
                            ReplyKeyboardRemove

                            
LANGUAGES_UZ = "🇺🇿 O'zbekcha"
LANGUAGES_RU = "🇷🇺 Русский"
LANGUAGES_EN = "🏴󠁧󠁢󠁥󠁮󠁧󠁿 English"


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



