from aiogram.dispatcher import FSMContext
from aiogram import types
import asyncio

from create_bot import bot, dp
from config import logger

from . import manager
from . import util
from entities import User, MainMessage, AdditionalMessage
# from entities.states import Registration
from assets.texts import (
	user as u_txt,
	admin as a_txt
)
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
	# user_id = message["from"]["id"]
	await state.finish()

	user = User(
		user_id=message["from"]["id"],
		username=str(message["from"]["username"]),
		language=message["from"]["language_code"],
		first_name=message["from"]["first_name"]
	)

	user_exists = await manager.is_user_exists(user.user_id)

	if user_exists:
		await MainMessage.delete(user.user_id)
		await AdditionalMessage.delete(user.user_id)

	# 	if not await manager.is_phone_entered(user.user_id):
	# 		reply_markup = u_rkb.request_contact
	# 	elif await manager.is_registered(user.user_id):
	# 		reply_markup = u_rkb.base  #u_rkb.registered
	# 	else:
	# 		reply_markup = u_rkb.base

	# 	await message.answer(u_txt.existing_user_greeting.format(first_name=user.first_name), reply_markup=reply_markup)
		await bot.send_message(381906725, a_txt.existing_user_greeting.format(user_id=user.user_id, username=user.username))

	# else:
	# 	registered = await manager.new_user(user)

	# 	if not registered: 
	# 		logger.error(f"{user.user_id}: {registered=}")
	# 		await message.answer(u_txt.error)
	# 		return


	# 	msg = await message.answer(u_txt.new_user_greeting.format(first_name=user.first_name), reply_markup=u_ikb.start_info)
	# 	await MainMessage.acquire(msg)

	# 	await bot.send_message(381906725, a_txt.new_user_greeting.format(user_id=user.user_id, username=user.username))

	# 	await asyncio.sleep(180)

	# 	try:
	# 		await message.answer(u_txt.channel_adv, reply_markup=u_ikb.channel_link)
	# 	except:
	# 		pass



# @logger.catch
# async def available_courses(message: types.Message, state: FSMContext):
# 	"""
# 	'Посмотреть курсы' reply keyboard
# 	Send info message
# 	"""
# 	user_id = message["from"]["id"]
# 	await state.finish()

# 	await AdditionalMessage.delete(user_id)

# 	msg = await util.send_photo(user_id, u_txt.description_png_picture)
# 	await AdditionalMessage.acquire(msg)
# 	msg = await message.answer(u_txt.available_courses, reply_markup=u_ikb.available_courses)
# 	await MainMessage.acquire(msg)



# @logger.catch
# async def who_are_we(message: types.Message, state: FSMContext):
# 	"""
# 	'Кто мы?' reply keyboard
# 	Send info message
# 	"""
# 	user_id = message["from"]["id"]
# 	await state.finish()

# 	await util.send_photo(user_id, photo=u_txt.who_are_we_picture)
# 	await message.answer(u_txt.who_are_we)
# 	await AdditionalMessage.delete(user_id)



# @logger.catch
# async def teachers(message: types.Message, state: FSMContext):
# 	"""
# 	'Преподаватели' reply keyboard
# 	Send info message
# 	"""
# 	user_id = message["from"]["id"]
# 	await state.finish()

# 	await util.send_photo(user_id, photo=u_txt.teachers_picture)
# 	await message.answer(u_txt.teachers)
# 	await AdditionalMessage.delete(user_id)



# @logger.catch
# async def our_goals(message: types.Message, state: FSMContext):
# 	"""
# 	'Почему мы создали этот вебинар' reply keyboard
# 	Send info message
# 	"""
# 	user_id = message["from"]["id"]
# 	await state.finish()

# 	await util.send_photo(user_id, photo=u_txt.our_goals_picture)
# 	await message.answer(u_txt.our_goals)
# 	await AdditionalMessage.delete(user_id)


 
# @logger.catch
# async def registration(message: types.Message, state: FSMContext):
# 	"""
# 	'Регистрация' reply keyboard
# 	Send info message and start
# 	Ragistration state
# 	"""
# 	user_id = message["from"]["id"]
# 	await state.finish()

# 	registered = await manager.is_registered(user_id)
# 	if registered:
# 		await message.answer(u_txt.already_registered)
# 		return		

# 	await message.answer(u_txt.registration_full_name)
# 	await Registration.full_name.set()
# 	await AdditionalMessage.delete(user_id)


# @logger.catch
# async def buy_subscription(message: types.Message, state: FSMContext):
# 	"""
# 	"Купить подписку" reply keyboard
# 	Checks if user has entered phone and registered
# 	Send info message and payment methods
# 	"""
# 	user_id=message["from"]["id"]
# 	await state.finish()
# 	await AdditionalMessage.delete(user_id)

# 	if not await manager.is_registered(user_id):
# 		await message.answer(u_txt.forbidden_not_registered, reply_markup=u_rkb.base)
# 		return
		
# 	if not await manager.is_phone_entered(user_id):
# 		await message.answer(u_txt.forbidden_not_entered_phone, reply_markup=u_rkb.request_contact)
# 		return

# 	msg = await message.answer(u_txt.buy_subscription, reply_markup=u_ikb.course_purchase)
# 	await MainMessage.acquire(msg)



