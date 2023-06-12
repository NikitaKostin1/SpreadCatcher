from create_bot import Dispatcher
from aiogram import types
from config import logger

# from entities.states import Registration
# from entities import Courses
from . import client



@logger.catch
def register_commands_handlers(dp: Dispatcher):
	"""
	Register all users commands
	"""
	# COMMANDS
	dp.register_message_handler(client.start, commands=["start"], state="*", chat_type=types.ChatType.PRIVATE)


	# REPLY KEYBOARD
	dp.register_message_handler(client.channel, lambda message: message.text == "🖊 Канал", state="*", chat_type=types.ChatType.PRIVATE)
	dp.register_message_handler(client.support, lambda message: message.text == "👨‍💻 Поддержка", state="*", chat_type=types.ChatType.PRIVATE)
	dp.register_message_handler(client.rates, lambda message: message.text == "🟢 АКТИВИРОВАТЬ PREMIUM 🟢", state="*", chat_type=types.ChatType.PRIVATE)

	dp.register_message_handler(client.parametres, lambda message: message.text == "⚙️ Настройки", state="*", chat_type=types.ChatType.PRIVATE)
	