from asyncpg.connection import Connection
from datetime import datetime, timedelta
from config import logger

from entities import User



@logger.catch
async def is_user_exists(connection: Connection, user_id: int) -> bool:
	"""
	Checks if user exists in database by chat_id
	"""
	record = await connection.fetchrow(
		f"SELECT * FROM users WHERE user_id = {user_id};"
	)
	return bool(record)



@logger.catch
async def get_user(connection: Connection, user_id: int) -> User:
	"""
	Return User object from users
	In error case return None
	"""
	try:
		record = await connection.fetchrow(f"""
			SELECT * FROM users WHERE user_id = {user_id};
		""")
		if not record: return None

		user = User(
			user_id=record.get("user_id"),
			username=record.get("username"),
			entry_date=record.get("entry_date"),
			is_bot_on=record.get("is_bot_on"),
			is_subscription_active=record.get("is_subscription_active"),
			subscription_id=record.get("subscription_id"),
			subscription_begin_date=record.get("subscription_begin_date"),
			is_test_active=record.get("is_test_active"),
			test_begin_date=record.get("test_begin_date")
		)

		return user
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return None


@logger.catch
async def set_new_user(connection: Connection, user: User) -> bool:
	"""
	Inserts new user into database
	"""
	try:
		# username column has VARCHAR(50) type
		if len(user.username) > 50:
			user.username = user.username[:50]

		await connection.execute(f"""
			BEGIN TRANSACTION ISOLATION LEVEL repeatable read;
			INSERT INTO users (
				user_id, username, entry_date, is_bot_on, 
				is_subscription_active, is_test_active
			) VALUES(
				{user.user_id}, '{user.username}',
				'{user.entry_date}', false, false, false
			);
			INSERT INTO users_parametres VALUES(
				{user.user_id}, NULL, 
				'QIWI Tinkoff YandexMoney Payeer AdvCash Sberbank SBP Alfa-bank RaiffeisenBank RosBank',
				'Binance Bitzlato Huobi Bybit OKX LocalBitcoin',
				1.0, 'Taker', 'Maker', 'USDT BTC ETH', 'RUB', 'p2p'
			);
			COMMIT;
		""")
		
		return True
	except Exception as e:
		logger.error(f"{user.user_id}: {e}")
		return False

