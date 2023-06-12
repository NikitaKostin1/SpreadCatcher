from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


channel_kb = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text="📢 Канал", url="https://t.me/SpreadCatchers")
b2 = InlineKeyboardButton(text="👨‍🔧 Поддержка", url="https://t.me/SC_Bot_Support")
channel_kb.row(b1, b2)

payment_option = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text="💸 Переводом", url="https://t.me/SC_Bot_Support")
b2 = InlineKeyboardButton(text="🪙 USDT", url="https://t.me/SC_Bot_Support")
b3 = InlineKeyboardButton(text="💳 Картой", url="https://t.me/SC_Bot_Support")
b4 = InlineKeyboardButton(text="🏦 Рассрочка", url="https://t.me/SC_Bot_Support")
payment_option.row(b1, b2).row(b3, b4)