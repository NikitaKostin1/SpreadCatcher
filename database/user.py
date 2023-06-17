from asyncpg.connection import Connection
from datetime import datetime, timedelta
from typing import Union
from config import logger

from entities import (
	User, StandardParametres,
	Parametres, Parameter
)



@logger.catch
async def is_user_exists(connection: Connection, user_id: int) -> bool:
	"""
	Checks if a user exists in the database by user_id
	"""
	record = await connection.fetchrow(
		f"SELECT * FROM users WHERE user_id = {user_id};"
	)
	return bool(record)


@logger.catch
async def get_user(connection: Connection, user_id: int) -> User:
	"""
	Returns a User object from the users table.
	Returns None in case of an error.
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
async def get_user_parametres(connection: Connection, user_id: int) -> Parametres:
	"""
	Returns a Parametres object from the users_parametres table.
	Returns None in case of an error.
	"""
	try:
		record = await connection.fetchrow(f"""
			SELECT * FROM users_parametres WHERE user_id = {user_id};
		""")
		if not record: return None

		parametres = Parametres(
			limits=record.get("limits"),
			banks=record.get("banks"),
			markets=record.get("markets"),
			spread=record.get("spread"),
			bid_type=record.get("bid_type"),
			ask_type=record.get("ask_type"),
			currencies=record.get("currencies"),
			fiat=record.get("fiat"),
			trading_type=record.get("trading_type")
		)

		return parametres
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return None


@logger.catch
async def get_parameter(connection: Connection, user_id: int, ParameterType: Parameter) -> Parameter:
	"""

	"""
	try:
		record = await connection.fetchrow(f"""
			SELECT {ParameterType.title} FROM users_parametres WHERE user_id = {user_id};
		""")
		param = ParameterType(record.get(ParameterType.title))

		return param
	except Exception as e:
		logger.error(f"{user_id}, {ParameterType}: {e}")
		return None	



@logger.catch
async def set_new_user(connection: Connection, user: User) -> bool:
	"""
	Inserts a new user into the database.
	"""
	try:
		# username column has VARCHAR(50) type
		if len(user.username) > 50:
			user.username = user.username[:50]

		params = StandardParametres()
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
				{user.user_id}, 
				{"NULL" if not params.limits.value else params.limits.value},
				'{" ".join(params.banks.value)}',
				'{" ".join(params.markets.value)}',
				{params.spread.value},
				'{params.bid_type.value}',
				'{params.ask_type.value}',
				'{" ".join(params.currencies.value)}',
				'{params.fiat.value}',
				'{params.trading_type.value}'
			);
			COMMIT;
		""")
		
		return True
	except Exception as e:
		logger.error(f"{user.user_id}: {e}")
		return False


@logger.catch
async def update_user_parametres(connection: Connection, user_id: int, params: Parametres) -> bool:
	"""
	Updates a user's parameters in the database.
	Returns a boolean value indicating the success of the operation
	"""
	try:
		await connection.execute(f"""
			BEGIN TRANSACTION ISOLATION LEVEL repeatable read;
			UPDATE users_parametres
			SET 
				limits={"NULL" if not params.limits.value else params.limits.value},
				banks='{" ".join(params.banks.value)}',
				markets='{" ".join(params.markets.value)}',
				spread={params.spread.value},
				bid_type='{params.bid_type.value}',
				ask_type='{params.ask_type.value}',
				currencies='{" ".join(params.currencies.value)}',
				fiat='{params.fiat.value}',
				trading_type='{params.trading_type.value}'
			WHERE user_id = {user_id};
			COMMIT;
		""")

		return True
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False


@logger.catch
async def update_user_parameter(connection: Connection, user_id: int, column: str, data: Union[str, int]) -> bool:
	"""
	Updates a user's parameter in the database.
	Returns a boolean value indicating the success of the operation
	"""
	try:
		await connection.execute(f"""
			BEGIN TRANSACTION ISOLATION LEVEL repeatable read;
			UPDATE users_parametres
			SET 
				{column} = {data}
			WHERE user_id = {user_id};
			COMMIT;
		""")

		return True
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False