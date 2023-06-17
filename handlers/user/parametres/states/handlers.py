from aiogram.dispatcher import FSMContext
from aiogram import types

from config import logger
from create_bot import bot

from . import input_checkers as checker

from ... import manager
from .. import util
from entities import (
	MainMessage, AdditionalMessage,
	Parametres, Parameter, InputError
)
from assets import texts as txt
from keyboards.user import (
	inline as ikb
)




@logger.catch
async def limits(message: types.Message, state: FSMContext):
	"""
	Handle the input for limits and check its validity.
	"""
	user_id = message["from"]["id"]
	user_input = message["text"]

	result = await checker.limits(user_input)

	if isinstance(result, InputError):
		msg = await message.answer(
			result.message,
			reply_markup=ikb.back_to_parametres
		)
		await AdditionalMessage.acquire(msg)
		return
	else:
		limits = result

	await state.finish()

	LimitsType = Parametres.get_annotations()["limits"]
	new_param = LimitsType(limits)

	await util.save_parameter(user_id, new_param)



@logger.catch
async def spread(message: types.Message, state: FSMContext):
	"""
	Handle the input for spread and check its validity.
	"""
	user_id = message["from"]["id"]
	user_input = message["text"]

	result = await checker.spread(user_id, user_input)

	if isinstance(result, InputError):
		msg = await message.answer(
			result.message,
			reply_markup=ikb.back_to_parametres
		)
		await AdditionalMessage.acquire(msg)
		return
	else:
		spread = result

	await state.finish()

	SpreadType = Parametres.get_annotations()["spread"]
	new_param = SpreadType(spread)

	await util.save_parameter(user_id, new_param)