from datetime import datetime
# from aiogram.dispatcher import FSMContext
from aiogram import types
# from datetime import datetime
import asyncio

from create_bot import bot, dp
from config import logger

from ..user import manager as user_manager
from . import manager
# from . import util
from entities import (
	MainMessage, AdditionalMessage,
	User, Subscriptions
)
from assets.texts import (
	user as u_txt,
	admin as a_txt
)
from keyboards.user import (
	reply as u_rkb
	# inline as u_ikb
)



@logger.catch
async def give_access(message: types.Message):
	try:
		user_id = int(message["text"].split()[1])
		subscription_id = int(message["text"].split()[2])
	except:
		# TODO: error message
		await message.answer("Неверная команда.")
		return

	user = await user_manager.get_user(user_id)

	if not user:
		# TODO: error message
		await message.answer("Этот пользователь ещё не зашёл в бота. Возможно неверно указан id")
		return

	subscription = Subscriptions.by_id(subscription_id)

	if not subscription:
		await message.answer("""
			Неверно указан id подписки. Варианты: 
			0 - Тестер
			1 - 1 месяц
			2 - 3 месяца
			3 - бессрочно
		""")
		return

	new_user = User(
		user_id=user_id,
		username=user.username,
		entry_date=user.entry_date,
		is_bot_on=False,
		is_subscription_active=True,
		subscription_id=subscription_id,
		subscription_begin_date=datetime.now(),
		is_test_active=False,
		test_begin_date=user.test_begin_date
	)

	user_updated = await manager.update_user(new_user)

	if not user_updated:
		# TODO: error message
		await message.answer("Ошибка!")
		return

	
	await message.answer(
		a_txt.access_given.format(
			username=user.username,
			user_id=user_id,
			title=subscription.title
		)
	)
	await bot.send_message(
		381906725, 
		a_txt.access_given.format(
			username=user.username,
			user_id=user_id,
			title=subscription.title
		)
	)
	
	await bot.send_message(user_id, u_txt.payment_success, reply_markup=u_rkb.active_subscription)
