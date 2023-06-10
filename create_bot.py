from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

import config


storage = MemoryStorage()

# Bot initialization
bot = Bot(token=config.TOKEN, parse_mode="html")
dp = Dispatcher(bot, storage=storage)

