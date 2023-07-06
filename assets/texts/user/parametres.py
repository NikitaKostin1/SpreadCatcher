signals_type_option = """
Выберите подходящий тип торговли
"""


parametres = """ \
Настройки параметров аккаунта <b>SCBot pro</b>:
  
• <b>Сумма банка:</b> {limits}
• <b>Платёжные системы:</b> {banks}
• <b>Криптовалюты:</b> {currencies}
• <b>Выбранные биржи:</b> {markets}
• <b>Сигналы со спредом:</b> >{spread}%
• <b>Тип торговли:</b> {bid_type} - {ask_type}
• <b>Фиатная валюта:</b> {fiat}

Обращаем Ваше внимание - результат работы НАПРЯМУЮ зависит от заданных Вами настроек <b>SCBot</b>!

Для изменения выберите кнопку 👇
"""

tester_restriction = """
У вас тестовый режим!
"""
tester_limits_restriction = """
Ваши лимиты исключительно любые!
"""
tester_currencies_restriction = """
Вам доступно только все монеты!
"""
tester_markets_restriction = """
Вам доступно только все банки!
"""
tester_spread_restriction = """
Ваш спред не может быть выше 1.0%
"""
tester_bid_ask_restriction = """
Вам доступна только позиция Taker - Maker!
"""



limits_info = """ 
Введите сумму банка с которой Вы готовы работать:
<code>Для "любой" суммы введите 0</code>
"""
limits_type_error = """
Неверный ввод!
Вы можете вводить только целые числа, пример:
<code>15 000</code> | <code>10000</code> | <code>25000</code>
"""
limits_min_error = """
Минимальная сумма банка 500р, c настройками ниже вы не найдёте связок.
"""
limits_max_error = """
Максимальная сумма банка 100,000р, c настройками выше вы не найдёте связок.
"""

banks_info = """
Выберите подходящие для Вас банки: 
• {banks}
"""

currencies_info = """
Выберите подходящие для Вас криптовалюты: 
• {currencies}
"""

markets_info = """
Выберите подходящие для Вас криптобиржи 
• {markets}
"""

spread_info = """ 
Введите спред, выше которого Вы хотите получать уведомления:
"""
spread_type_error = """
Неверный ввод!
Вы можете вводить только целые и дробные цифры, пример:
<code>0.75</code> | <code>2</code> | <code>3.1</code>
"""
spread_min_error = """
Минимальный спред 0.5%, c настройками ниже вы слишком много связок.
"""
spread_max_error = """
Максимальный спред 5%, c настройками выше вы не найдёте связок.
"""

trading_type_info = """
Выберите подходящий для Вас тип сделок: 
• {bid_type} - {ask_type}
"""

fiat_info = """
Выберите подходящую для Вас фиатную валюту: 
• {fiat}
"""

