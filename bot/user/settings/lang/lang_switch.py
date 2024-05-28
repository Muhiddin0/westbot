
from aiogram import types
from aiogram.dispatcher import FSMContext

from asyncio import create_task

from loader import dp
from asgiref.sync import sync_to_async
from utils import button, texts
from states import UpdateRegister
from bot.models import User
from utils import buttons, texts

async def lang_task(callback: types.CallbackQuery, state: FSMContext):
    """
    Ro'yxatdan o'tmagan userni ro'yxatdan o'tqazishni boshlash va
    Bu yerda userni tili aniqlanadi
    """

    # user id
    user_id = callback.message.from_user.id
    lang = callback.data
    user = await sync_to_async(User.objects.get)(user_id=user_id)
    
    lang_codes = {
        buttons.LANGUAGES_UZ: 'uz',
        buttons.LANGUAGES_RU: 'ru',
        buttons.LANGUAGES_EN: 'en'
    }

    if not lang in lang_codes: 
        """
        Agar user xato til kiritsa
        """
        await callback.message.delete()
        return
    
    # til codeni olish
    lang = lang_codes[lang]
    
    # olingan til codeni statega joylash
    await state.set_data({
        'lang': lang
    })
    state_data = await state.get_data()
    lang = state.set_data['lang']
    user.lang = lang
    await sync_to_async(user.save)()
    await callback.message.delete()


    if user.lang == 'uz':
        await callback.message.answer(
            text=texts.LANG_SWITCH_HANDLER[lang],
            reply_markup=buttons.MAIN_MENU(lang)
        )
    elif user.lang == 'ru':
        await callback.message.answer(
            text=texts.LANG_SWITCH_HANDLER[lang],
            reply_markup=buttons.MAIN_MENU(lang)
        )
    elif user.lang == 'en':
        await callback.message.answer(
            text=texts.LANG_SWITCH_HANDLER[lang],
            reply_markup=buttons.MAIN_MENU(lang)
        )
    # change state to phone number
    await state.finish()

    # userdan telefon raqamini yuborishni so'rash
    
    # stateni telefon raqamiga o'tqazish
    await state.finish()
    

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=UpdateRegister.lang)
async def lang(message: types.Message, state: FSMContext):
    create_task(lang_task(message, state))
