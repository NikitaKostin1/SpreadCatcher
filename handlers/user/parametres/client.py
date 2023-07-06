from aiogram import types

from create_bot import bot
from config import logger

from .. import manager
from . import util
from entities import (
	MainMessage, AdditionalMessage,
	User, Parametres
)
from entities.states import (
	Limits, Spread
)
from assets import texts as txt
from keyboards.user import (
	inline as ikb
)



@logger.catch
async def menu(callback: types.CallbackQuery):
	"""
	Sets signals type as `p2p`
	Handles the 'parametres_menu' callback. Displays the user's parameters.
	"""
	user_id = callback["message"]["chat"]["id"]
	await MainMessage.delete(user_id)

	SignalsType = Parametres.get_annotations()["signals_type"]
	signals_type = SignalsType("p2p")

	await util.save_parameter(user_id, signals_type)

	is_bot_on = await manager.is_bot_on(user_id)
	if is_bot_on:
		bot_disabled = await manager.disable_bot(user_id)
		await callback.message.answer(txt.bot_disabled)
		await callback.message.answer(txt.bot_disabling_info)

	text = await util.parametres_text(user_id)

	if not text:
		await callback.message.answer(txt.error)
		return

	msg = await callback.message.answer(text, reply_markup=ikb.parametres)
	await MainMessage.acquire(msg)



@logger.catch
async def limits(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'limits' button in the parametres menu.
	Deletes the menu message markup and starts the input state for entering limits. 
	If user is tester sends notification message
	"""
	user_id = callback["message"]["chat"]["id"]

	is_tester = await manager.is_tester(user_id)
	if is_tester:
		await callback.answer(txt.tester_restriction)
		return

	await callback.answer()
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	msg = await callback.message.answer(
		txt.limits_info, reply_markup=ikb.back_to_parametres
	)
	await AdditionalMessage.acquire(msg)

	await Limits.limits.set()


@logger.catch
async def banks(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'banks' button in the parametres menu.
	Retrieves the banks parameter value for the user and displays it with the corresponding markup.
	"""
	user_id = callback["message"]["chat"]["id"]

	await callback.answer()
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	BanksType = Parametres.get_annotations()["banks"]
	banks = await manager.get_parameter(user_id, BanksType)

	if not banks:
		await callback.answer(txt.error)
		return

	markup = ikb.parametres_banks
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), banks.value
	)

	msg = await callback.message.answer(
		txt.banks_info.format(banks=" | ".join(banks.value)),
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg)




@logger.catch
async def currencies(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'currencies' button in the parametres menu.
	Retrieves the currencies parameter value for the user and displays it with the corresponding markup.
	"""
	user_id = callback["message"]["chat"]["id"]

	is_tester = await manager.is_tester(user_id)
	if is_tester:
		await callback.answer(txt.tester_restriction)
		return

	await callback.answer()
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	CurrenciesType = Parametres.get_annotations()["currencies"]
	currencies = await manager.get_parameter(user_id, CurrenciesType)

	if not currencies:
		await callback.answer(txt.error)
		return

	markup = ikb.parametres_currencies
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), currencies.value
	)

	msg = await callback.message.answer(
		txt.currencies_info.format(currencies=" | ".join(currencies.value)),
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg)



@logger.catch
async def markets(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'markets' button in the parametres menu.
	Retrieves the markets parameter value for the user and displays it with the corresponding markup.

	"""
	user_id = callback["message"]["chat"]["id"]

	is_tester = await manager.is_tester(user_id)
	if is_tester:
		await callback.answer(txt.tester_restriction)
		return

	await callback.answer()
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	MarketsType = Parametres.get_annotations()["markets"]
	markets = await manager.get_parameter(user_id, MarketsType)

	if not markets:
		await callback.answer(txt.error)
		return

	markup = ikb.parametres_markets
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), markets.value
	)

	msg = await callback.message.answer(
		txt.markets_info.format(markets=" | ".join(markets.value)),
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg)



@logger.catch
async def spread(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'spread' button in the parametres menu.
	Deletes the menu message markup and starts the input state for entering the spread.
	"""
	await callback.answer()

	user_id = callback["message"]["chat"]["id"]
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	msg = await callback.message.answer(
		txt.spread_info, reply_markup=ikb.back_to_parametres
	)
	await AdditionalMessage.acquire(msg)

	await Spread.spread.set()


@logger.catch
async def trading_type(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'trading_type' button in the parametres menu.
	Retrieves the trading_type parameter value for the user and displays it with the corresponding markup.
	"""
	user_id = callback["message"]["chat"]["id"]

	is_tester = await manager.is_tester(user_id)
	if is_tester:
		await callback.answer(txt.tester_restriction)
		return

	await callback.answer()
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	BidType = Parametres.get_annotations()["bid_type"]
	AskType = Parametres.get_annotations()["ask_type"]
	bid_type = await manager.get_parameter(user_id, BidType)
	ask_type = await manager.get_parameter(user_id, AskType)

	if not bid_type or not ask_type:
		await callback.answer(txt.error)
		return

	trading_type = f"{bid_type.value}-{ask_type.value}"
	markup = ikb.parametres_trading_type
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), [trading_type]
	)

	msg = await callback.message.answer(
		txt.trading_type_info.format(
			bid_type=bid_type.value, ask_type=ask_type.value
		),
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg)


@logger.catch
async def fiat(callback: types.CallbackQuery):
	"""
	Handle the callback when the user clicks on the 'fiat' button in the parametres menu.
	Retrieves the fiat parameter value for the user and displays it with the corresponding markup.
	"""
	user_id = callback["message"]["chat"]["id"]

	await callback.answer()
	await MainMessage.edit(user_id, await util.parametres_text(user_id))

	FiatType = Parametres.get_annotations()["fiat"]
	fiat = await manager.get_parameter(user_id, FiatType)

	if not fiat:
		await callback.answer(txt.error)
		return

	markup = ikb.parametres_fiat
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), [fiat.value]
	)

	msg = await callback.message.answer(
		txt.fiat_info.format(fiat=fiat.value),
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg)