import logging
import os
from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()


TEST_BOT = "7051414083:AAHpBU6u5acYtJTcwyyclm3-DJJzUIJme-c"
API_TOKEN = os.getenv('BOT_TOKEN') or TEST_BOT

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)