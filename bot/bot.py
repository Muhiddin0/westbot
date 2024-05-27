
from aiogram import executor
from loader import dp, bot

import user

async def on_startup(dp):
    # Adminlarga xabar yuborish
    ADMIN = 5765144405
    await bot.send_message(ADMIN, "Bot ishga tushdi!")

# disable skip_update deploy version
executor.start_polling(dp, skip_updates=False, on_startup=on_startup)