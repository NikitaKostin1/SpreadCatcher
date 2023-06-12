from aiogram import types
from create_bot import Dispatcher
from config import logger

from . import client



@logger.catch
def register_commands_handlers(dp: Dispatcher):
	"""
	Register all admins commands
	"""
	dp.register_message_handler(client.give_access, lambda message: message.text.split()[0] == "Доступ7358", state="*", chat_type=types.ChatType.PRIVATE)
