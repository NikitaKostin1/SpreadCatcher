from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import astuple

from entities import StandardParametres



available_banks = StandardParametres().banks.available_values
available_markets = StandardParametres().markets.available_values
available_currencies = StandardParametres().currencies.available_values
available_bid_types = StandardParametres().bid_type.available_values
available_ask_types = StandardParametres().ask_type.available_values
available_fiats = StandardParametres().fiat.available_values
available_trading_types = StandardParametres().trading_type.available_values


channel_kb = InlineKeyboardMarkup(row_width=2)
channel = InlineKeyboardButton(text="📢 Канал", url="https://t.me/SpreadCatchers")
support = InlineKeyboardButton(text="👨‍🔧 Поддержка", url="https://t.me/SC_Bot_Support")
channel_kb.row(channel, support)

test_drive = InlineKeyboardMarkup(row_width=1)
start = InlineKeyboardButton(text="Начать тест-драйв", callback_data="test_drive")
test_drive.add(start)

payment_option = InlineKeyboardMarkup(row_width=2)
transfer = InlineKeyboardButton(text="💸 Переводом", url="https://t.me/SC_Bot_Support")
usdt = InlineKeyboardButton(text="🪙 USDT", url="https://t.me/SC_Bot_Support")
card = InlineKeyboardButton(text="💳 Картой", url="https://t.me/SC_Bot_Support")
installment = InlineKeyboardButton(text="🏦 Рассрочка", url="https://t.me/SC_Bot_Support")
payment_option.row(transfer, usdt).row(card, installment)

parametres = InlineKeyboardMarkup(row_width=3)
limits = InlineKeyboardButton(text="Сумма", callback_data="parametres limits")
banks = InlineKeyboardButton(text="Платёжные системы", callback_data="parametres banks")
currencies = InlineKeyboardButton(text="Криптовалюта", callback_data="parametres currencies")
markets = InlineKeyboardButton(text="Биржи", callback_data="parametres markets")
spread = InlineKeyboardButton(text="Спред", callback_data="parametres spread")
trading_type = InlineKeyboardButton(text="Тип торговли", callback_data="parametres trading_type")
fiat = InlineKeyboardButton(text="Фиат", callback_data="parametres fiat")
all_btns = [limits, banks, currencies, markets, spread, trading_type, fiat]
parametres.add(*all_btns)

back_to_parametres = InlineKeyboardMarkup(row_width=1)
back = InlineKeyboardButton(text="↩️ Назад", callback_data="back_to_parametres")
back_to_parametres.add(back)


parametres_banks = InlineKeyboardMarkup(row_width=3)
for bank in available_banks:
	bank_btn = InlineKeyboardButton(text=bank, callback_data=f"set_bank {bank}")
	parametres_banks.insert(bank_btn)
complete_btn = InlineKeyboardButton(text="Готово ✅", callback_data=f"set_bank complete")
parametres_banks.add(complete_btn)

parametres_currencies = InlineKeyboardMarkup(row_width=3)
for currency in available_currencies:
	currency_btn = InlineKeyboardButton(text=currency, callback_data=f"set_currency {currency}")
	parametres_currencies.insert(currency_btn)
complete_btn = InlineKeyboardButton(text="Готово ✅", callback_data=f"set_currency complete")
parametres_currencies.add(complete_btn)

parametres_markets = InlineKeyboardMarkup(row_width=3)
for market in available_markets:
	market_btn = InlineKeyboardButton(text=market, callback_data=f"set_market {market}")
	parametres_markets.insert(market_btn)
complete_btn = InlineKeyboardButton(text="Готово ✅", callback_data=f"set_market complete")
parametres_markets.add(complete_btn)

parametres_trading_type = InlineKeyboardMarkup(row_width=2)
for bid_type in available_bid_types:
	for ask_type in available_ask_types:
		trading_type_btn = InlineKeyboardButton(text=f"{bid_type}-{ask_type}", callback_data=f"set_trading_type {bid_type}-{ask_type}")
		parametres_trading_type.insert(trading_type_btn)
complete_btn = InlineKeyboardButton(text="Готово ✅", callback_data=f"set_trading_type complete")
parametres_trading_type.add(complete_btn)

parametres_fiat = InlineKeyboardMarkup(row_width=3)
for fiat in available_fiats:
	fiat_btn = InlineKeyboardButton(text=fiat, callback_data=f"set_fiat {fiat}")
	parametres_fiat.insert(fiat_btn)
complete_btn = InlineKeyboardButton(text="Готово ✅", callback_data=f"set_fiat complete")
parametres_fiat.add(complete_btn)


def get_signal_keyboard(bid_url: str, ask_url: str) -> InlineKeyboardMarkup:
	signal = InlineKeyboardMarkup(row_width=2)
	bid_btn = InlineKeyboardButton(text="Купить", url=bid_url)
	ask_btn = InlineKeyboardButton(text="Продать", url=ask_url)
	signal.row(bid_btn, ask_btn)

	return signal



