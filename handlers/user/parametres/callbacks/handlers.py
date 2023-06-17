from aiogram import types

from create_bot import bot
from config import logger

from ... import manager
from .. import util
from entities import (
	MainMessage, AdditionalMessage,
	User, Parametres
)

from assets import texts as txt
from keyboards.user import (
	inline as ikb
)



@logger.catch
async def banks(callback: types.CallbackQuery):
	"""
	Handle the callback for banks and check its validity.
	"""
	user_id = callback["message"]["chat"]["id"]
	await callback.answer()

	button_value = callback["data"].split()[1]
	message = await AdditionalMessage.get_message(user_id)

	if not message:
		await callback.message.delete()
		return

	message_markup = message.reply_markup
	chosen_banks: list = util.get_markup_chosen_values(message_markup)

	if button_value == "complete":
		BanksType = Parametres.get_annotations()["banks"]
		new_param = BanksType(chosen_banks)

		await util.save_parameter(user_id, new_param)
		return
	else:
		bank = button_value


	if bank in chosen_banks:
		if len(chosen_banks) == 1:
			return
		chosen_banks.remove(bank)
	else:
		chosen_banks.append(bank)


	markup = ikb.parametres_banks
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), chosen_banks
	)
	
	message_text = txt.banks_info.format(banks=" | ".join(chosen_banks))
	msg = await AdditionalMessage.edit(
		user_id, message_text,
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg, message_text, edited_markup)


@logger.catch
async def currencies(callback: types.CallbackQuery):
	"""
	Handle the callback for currencies and check its validity.
	"""
	user_id = callback["message"]["chat"]["id"]
	await callback.answer()

	button_value = callback["data"].split()[1]
	message = await AdditionalMessage.get_message(user_id)

	if not message:
		await callback.message.delete()
		return

	message_markup = message.reply_markup
	chosen_currencies: list = util.get_markup_chosen_values(message_markup)


	if button_value == "complete":
		CurrenciesType = Parametres.get_annotations()["currencies"]
		new_param = CurrenciesType(chosen_currencies)

		await util.save_parameter(user_id, new_param)
		return
	else:
		currency = button_value


	if currency in chosen_currencies:
		if len(chosen_currencies) == 1:
			return
		chosen_currencies.remove(currency)
	else:
		chosen_currencies.append(currency)

	markup = ikb.parametres_currencies
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), chosen_currencies
	)


	message_text = txt.currencies_info.format(currencies=" | ".join(chosen_currencies))
	msg = await AdditionalMessage.edit(
		user_id, message_text,
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg, message_text, edited_markup)



@logger.catch
async def markets(callback: types.CallbackQuery):
	"""
	Handle the callback for markets and check its validity.
	"""
	user_id = callback["message"]["chat"]["id"]
	await callback.answer()

	button_value = callback["data"].split()[1]
	message = await AdditionalMessage.get_message(user_id)

	if not message:
		await callback.message.delete()
		return

	message_markup = message.reply_markup
	chosen_markets: list = util.get_markup_chosen_values(message_markup)


	if button_value == "complete":
		MarketsType = Parametres.get_annotations()["markets"]
		new_param = MarketsType(chosen_markets)

		await util.save_parameter(user_id, new_param)
		return
	else:
		market = button_value


	if market in chosen_markets:
		if len(chosen_markets) == 1:
			return
		chosen_markets.remove(market)
	else:
		chosen_markets.append(market)

	markup = ikb.parametres_markets
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), chosen_markets
	)


	message_text = txt.markets_info.format(markets=" | ".join(chosen_markets))
	msg = await AdditionalMessage.edit(
		user_id, message_text,
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg, message_text, edited_markup)


@logger.catch
async def trading_type(callback: types.CallbackQuery):
	"""
	Handle the callback for trading_type and check its validity.
	"""
	user_id = callback["message"]["chat"]["id"]
	await callback.answer()

	button_value = callback["data"].split()[1]
	message = await AdditionalMessage.get_message(user_id)

	if not message:
		await callback.message.delete()
		return

	message_markup = message.reply_markup
	chosen_trading_type: list = util.get_markup_chosen_values(message_markup)[0]
	chosen_bid_type, chosen_ask_type = chosen_trading_type.split("-")

	if button_value == "complete":
		BidType = Parametres.get_annotations()["bid_type"]
		AskType = Parametres.get_annotations()["ask_type"]
		new_bid_param = BidType(chosen_bid_type)
		new_ask_param = AskType(chosen_ask_type)

		await util.save_parameter(user_id, new_bid_param)
		await util.save_parameter(user_id, new_ask_param)
		return
	else:
		trading_type = button_value
		bid_type, ask_type = trading_type.split("-")

	markup = ikb.parametres_trading_type
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), trading_type
	)

	message_text = txt.trading_type_info.format(bid_type=bid_type, ask_type=ask_type)
	msg = await AdditionalMessage.edit(
		user_id, message_text,
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg, message_text, edited_markup)


@logger.catch
async def fiat(callback: types.CallbackQuery):
	"""
	Handle the callback for fiat and check its validity.
	"""
	user_id = callback["message"]["chat"]["id"]
	await callback.answer()

	button_value = callback["data"].split()[1]
	message = await AdditionalMessage.get_message(user_id)

	if not message:
		await callback.message.delete()
		return

	message_markup = message.reply_markup
	chosen_fiat: list = util.get_markup_chosen_values(message_markup)[0]

	if button_value == "complete":
		FiatType = Parametres.get_annotations()["fiat"]
		new_param = FiatType(chosen_fiat)

		await util.save_parameter(user_id, new_param)
		return
	else:
		fiat = button_value

	markup = ikb.parametres_fiat
	edited_markup = util.mark_markup_chosen_buttons(
		dict(markup).copy(), fiat
	)


	message_text = txt.fiat_info.format(fiat=fiat)
	msg = await AdditionalMessage.edit(
		user_id, message_text,
		reply_markup=edited_markup
	)
	await AdditionalMessage.acquire(msg, message_text, edited_markup)