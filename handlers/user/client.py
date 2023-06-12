from aiogram.dispatcher import FSMContext
from aiogram import types
from datetime import datetime
import asyncio

from create_bot import bot, dp
from config import logger

from . import manager
from . import util
from entities import (
	User, MainMessage, AdditionalMessage
)
from assets import texts as txt
from keyboards.user import (
	reply as u_rkb,
	inline as u_ikb
)



@logger.catch
async def start(message: types.Message, state: FSMContext):
	"""
	'/start' command
	If user isn't in database's table 'users' - inserts him
	"""
	await state.finish()

	user = User(
		user_id=message["from"]["id"],
		username=str(message["from"]["username"])
	)

	user_exists = await manager.is_user_exists(user.user_id)

	if user_exists:
		await MainMessage.delete(user.user_id)
		await AdditionalMessage.delete(user.user_id)

		if await manager.is_tester(user.user_id):
			reply_markup = u_rkb.tester
		elif await manager.is_subscription_active(user.user_id):
			reply_markup = u_rkb.active_subscription
		elif await manager.is_tester_expired(user.user_id):
			reply_markup = u_rkb.tester_expired
		else:
			reply_markup = u_rkb.new_user


		first_name = message["from"]["first_name"]
		await message.answer(
			txt.existing_user_greeting.format(first_name=first_name), 
			reply_markup=reply_markup
		)
		await bot.send_message(
			381906725, 
			txt.existing_user_greeting.format(
				user_id=user.user_id, username=user.username
			)
		)

	else:
		user.entry_date = datetime.now()
		registered = await manager.set_new_user(user)

		if not registered: 
			logger.error(f"{user.user_id}: {registered=}")
			await message.answer(txt.error)
			return

		await message.answer(
			txt.new_user_greeting, reply_markup=u_rkb.new_user
		)
		msg = await message.answer(
			txt.faq, reply_markup=u_ikb.channel_kb, 
			disable_web_page_preview=True
		)
		await MainMessage.acquire(msg)

		await bot.send_message(
			381906725, 
			txt.new_user_greeting.format(
				user_id=user.user_id, username=user.username
			)
		)




@logger.catch
async def parametres(message: types.Message, state: FSMContext):
	await state.finish()
	user_id = message["from"]["id"]






@logger.catch
async def channel(message: types.Message, state: FSMContext):
	await state.finish()
	user_id = message["from"]["id"]

	msg = await util.send_photo(
		user_id,
		photo="AgACAgQAAxkDAAEFaMRjAAE92sIDlXKKItUBN2yiy2e78vIAAii5MRtsnwABUA-Hs0UXPXreAQADAgADeAADKQQ",
		caption=txt.channel_link
	)
	await MainMessage.acquire(msg)
	

@logger.catch
async def support(message: types.Message, state: FSMContext):
	await state.finish()
	user_id = message["from"]["id"]

	msg = await util.send_photo(
		user_id, 
		photo="AgACAgQAAxkDAAEFaMhjAAE95GLbtIzfRI5N_OHTQDGDGl4AAim5MRtsnwABUGE6F6MLZ-usAQADAgADeAADKQQ",
		caption=txt.support_link
	)
	await MainMessage.acquire(msg)


@logger.catch
async def rates(message: types.Message, state: FSMContext):
	await state.finish()
	user_id = message["from"]["id"]

	msg = await message.answer(
		txt.rates,
		reply_markup=u_ikb.payment_option,
		disable_web_page_preview=True
	)
	await MainMessage.acquire(msg)


