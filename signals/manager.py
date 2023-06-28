from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.exceptions import BotBlocked
from handlers.user import manager as user_manager
from assets import texts as txt
from create_bot import bot
from config import logger
import asyncio

from keyboards.user import (
	inline as ikb
)

from typing import NoReturn, Tuple
from entities.parsing.types import (
	ParserResponse
)
from entities import (
	Parser,
	BinanceParser, HuobiParser,
	BybitParser, OkxParser, PexpayParser,
	Parametres
)



@logger.catch
async def notificate_user(user_id: int) -> NoReturn:
	"""
	Send a notification to the user about inefficient parameters
	"""
	try:
		await bot.send_message(user_id, txt.inefficient_parametres)
	except BotBlocked:
		await user_manager.disable_bot(user_id)



@logger.catch
async def gather_parsers_responses(
	currency: str, parametres: Parametres
) -> Tuple[ParserResponse]:
	""""
	Gather responses from parsers for the specified currency and parameters.

	Args:
		currency (str): The currency to gather responses for.
		parametres (Parametres): The parameters to use for parsing.

	Returns:
		Tuple[ParserResponse]: A tuple of ParserResponse objects representing the responses from parsers.
	"""
	parsers = {
		"Binance": BinanceParser,
		"Huobi": HuobiParser,
		"Bybit": BybitParser, 
		"OKX": OkxParser,
		"PexPay": PexpayParser
	}
	parsers_responses = list()

	for market in parametres.markets.value:
		MarketParser: Parser = parsers[market]

		parser = MarketParser(
			fiat=parametres.fiat.value,
			currency=currency,
			banks=parametres.banks.value,
			limits=parametres.limits.value
		)
		response: ParserResponse = await parser.get_p2p()
		parsers_responses.append(response)

	return tuple(parsers_responses)


@logger.catch	
async def send_signal(
	user_id: int, parametres: Parametres,
	bid: ParserResponse, ask: ParserResponse
) -> bool:
	"""
	Send a signal to the user if the spread meets the parameters.

	Args:
		user_id (int): The ID of the user.
		parametres (Parametres): The parameters to use for signal filtering.
		bid (ParserResponse): The bid response from a parser.
		ask (ParserResponse): The ask response from a parser.

	Returns:
		bool: True if the signal is sent, False otherwise.
	"""
	scam_spread = 7

	bid_price = bid.conditions.price
	ask_price = ask.conditions.price
	spread = round((1 - bid_price / ask_price) * 100, 2)
	logger.success(f"{spread}% | {bid_price} - {ask_price}")

	# if spread > scam_spread:
	# 	# Scam
	# 	return False

	if spread < parametres.spread.value:
		return False

	text = txt.message.format(
		bid_market=bid.market,
		ask_market=ask.market,
		currency=bid.conditions.currency,
		bid_price=f"{bid.conditions.price:,.2f}",
		ask_price=f"{ask.conditions.price:,.2f}",
		spread=spread,
		bid_limits_min=f"{bid.conditions.limits_min:,}",
		bid_limits_max=f"{bid.conditions.limits_max:,}",
		bid_bank=bid.conditions.bank,
		ask_limits_min=f"{ask.conditions.limits_min:,}",
		ask_limits_max=f"{ask.conditions.limits_max:,}",
		ask_bank=ask.conditions.bank,
		fiat_symbol="p"
	)

	markup = await generate_markup(parametres, bid, ask)

	try:
		await bot.send_message(user_id, text, reply_markup=markup)
	except BotBlocked:
		await user_manager.disable_bot(user_id)

	return True



@logger.catch
async def iterate_advertisments(
	user_id: int, parametres: Parametres,
	responses: Tuple[ParserResponse]
) -> bool:
	"""
	Iterate through responses and send signals to the user for valid bid-ask pairs.

	Args:
		user_id (int): The ID of the user.
		parametres (Parametres): The parameters to use for signal filtering.
		responses (Tuple[ParserResponse]): The responses from parsers.

	Returns:
		bool: True if at least one signal is sent, False otherwise.
	"""
	logger.warning("Scam spread detection is turned off")
	sent_signals = 0

	for response in responses:
		bid = response.best_bid
		if bid is None:
			continue

		for response in responses:
			ask = response.best_ask
			if ask is None:
				continue

			is_signal_sent = await send_signal(user_id, parametres, bid, ask)
			sent_signals += int(is_signal_sent)
			await asyncio.sleep(0.4)

	return sent_signals




@logger.catch
async def generate_markup(
	parametres: Parametres, 
	bid: Advertisement, ask: Advertisement
) -> InlineKeyboardMarkup: 
	"""
	Generate an inline keyboard markup for the bid and ask responses

	Args:
		parametres (Parametres): The parameters used for parsing
		bid (Advertisement): The bid advertisement
		ask (Advertisement): The ask advertisement

	Returns:
		InlineKeyboardMarkup: The generated inline keyboard markup
	"""
	advertiser_id_bid = bid.advertiser.advertiser_id
	advertiser_id_ask = ask.advertiser.advertiser_id

	match bid.market:
		case "Binance":
			bid_url = f"https://p2p.binance.com/en/advertiserDetail?advertiserNo={advertiser_id_bid}"
		case "Huobi":
			bid_url = f"https://c2c.huobi.com/ru-ru/trader/{advertiser_id_bid}"
		case "Bybit":
			bid_url = f"https://www.bybit.com/fiat/trade/otc/?actionType=1&token={ask.conditions.currency}&fiat={ask.conditions.fiat}"
		case "OKX":
			bid_url = f"https://www.okx.com/ru/p2p/ads-merchant?publicUserId={advertiser_id_bid}"	
		case "PexPay":
			bid_url = f"https://www.pexpay.com/en/advertiserDetail?advertiserNo={advertiser_id_bid}"

	match ask.market:
		case "Binance":
			ask_url = f"https://p2p.binance.com/en/advertiserDetail?advertiserNo={advertiser_id_ask}"
		case "Huobi":
			ask_url = f"https://c2c.huobi.com/ru-ru/trader/{advertiser_id_ask}"
		case "Bybit":
			ask_url = f"https://www.bybit.com/fiat/trade/otc/?actionType=0&token={ask.conditions.currency}&fiat={ask.conditions.fiat}"
		case "OKX":
			ask_url = f"https://www.okx.com/ru/p2p/ads-merchant?publicUserId={advertiser_id_ask}"
		case "PexPay":
			ask_url = f"https://www.pexpay.com/en/advertiserDetail?advertiserNo={advertiser_id_ask}"

	return ikb.get_signal_keyboard(bid_url, ask_url)