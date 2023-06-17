from aiogram.utils.exceptions import BotBlocked
from datetime import timedelta
from typing import List
import asyncio

from config import logger
from create_bot import bot
from handlers.admin import (
	manager as admin_manager
)
from handlers.user import (
	manager as user_manager
)
from entities import (
	Subscriptions, User
)

from assets import texts as txt
from keyboards.user import (
	reply as rkb
)



@logger.catch
async def tester(wait_for: int):
	"""
	Check all users with active Tester subscription.
	If a user's Tester term has expired according to the Tester.term timedelta,
	it sets the user as expired and sends a notification message.
	"""
	while True:
		users: List[User] = await admin_manager.get_tester_users()

		for user in users:
			is_expired = await user_manager.is_tester_expired(user.user_id)
			if is_expired:

				# TODO: Turn off the bot
				access_closed = await admin_manager.set_tester_as_expired(user.user_id)
				if not access_closed:
					# TODO: Error message
					await bot.send_message(
						381906725, f"ТЕСТЕР НЕ ОТКЛЮЧИЛСЯ <code>{user.user_id}</code>"
					)

				try:
					await bot.send_message(
						user.user_id, txt.tester_expired, 
						reply_markup=rkb.tester_expired
					)
				except BotBlocked:
					pass

		await asyncio.sleep(wait_for)



