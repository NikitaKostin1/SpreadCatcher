from config import logger, get_conn

from datetime import datetime, timedelta
from typing import Tuple

from entities import (
	User, Subscriptions,
	Parametres, Parameter
)
from database import user as db



@logger.catch
async def is_user_exists(user_id: int) -> bool:
	"""
	Check if the user exists in the users table.
	"""
	try:
		connection = await get_conn()
		exists = await db.is_user_exists(connection, user_id)

		return exists
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False


@logger.catch
async def get_user(user_id: int) -> User:
	"""
	Retrieve the User object from the users table based on the user ID.
	Returns:
		The User object if found, None otherwise.
	"""
	try:
		connection = await get_conn()
		user: User = await db.get_user(connection, user_id)

		return user
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return None


@logger.catch
async def set_new_user(user: User) -> bool:
	"""
	Insert the user's data into the database.
	"""
	if not user.username or not user.entry_date:
		logger.error(""" \
			'username' or 'entry_date' parametres are not provided for the User instance!
		""")
		return False

	try:
		user.entry_date = datetime.now()
		connection = await get_conn()
		registered = await db.set_new_user(connection, user)

		return registered
	except Exception as e:
		logger.error(f"{user}: {e}")
		return False


@logger.catch
async def get_user_parametres(user_id: int) -> Parametres:
	"""
	Retrieve the Parametres object from the users_parametres table based on the user ID.
	Returns:
		The Parametres object if found, None otherwise.
	"""
	try:
		connection = await get_conn()
		parametres: Parametres = await db.get_user_parametres(connection, user_id)

		return parametres
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return None


@logger.catch
async def get_parameter(user_id: int, ParameterType: Parameter) -> Parameter:
	"""
	Retrieve the Parameter object from the users_parametres table 
	based on the user ID and Parameter type
	Returns:
		The Parameter object if found, None otherwise.
	"""
	try:
		connection = await get_conn()
		param = await db.get_parameter(connection, user_id, ParameterType)

		return param
	except Exception as e:
		logger.error(f"{user_id}, {ParameterType}: {e}")
		return None


@logger.catch
async def update_user_parametres(user_id: int, params: Parametres) -> bool:
	"""
	Update the user's parameters in the database.
	Args:
		user_id: The ID of the user.
		params: The Parametres object containing the updated parameters.
	"""
	try:
		connection = await get_conn()
		updated = await db.update_user_parametres(connection, user_id, params)

		return updated
	except Exception as e:
		logger.error(f"{user}: {e}")
		return False


@logger.catch
async def update_user_parameter(user_id: int, param: Parameter) -> bool:
	"""
	Update a specific parameter of the user in the database.
	Args:
		user_id: The ID of the user.
		param: The Parameter object representing the parameter to update.
	Returns:
		True if the update is successful, False otherwise.
	"""
	try:
		connection = await get_conn()

		if param.value is None:
			data = "NULL"
		elif isinstance(param.value, list):
			data = "'{}'".format(" ".join(param.value))
		elif isinstance(param.value, str):
			data = f"\'{param.value}\'"
		else:
			data = param.value

		updated = await db.update_user_parameter(connection, user_id, param.title, data)

		return updated
	except Exception as e:
		logger.error(f"{user}: {e}")
		return False



@logger.catch
async def is_subscription_active(user_id: int) -> bool:
	"""
	Check if the user's subscription is active.
	"""
	try:
		connection = await get_conn()
		user = await db.get_user(connection, user_id)

		return user.is_subscription_active
	except Exception as e:
		logger.error(f"{user}: {e}")
		return False


@logger.catch
async def is_tester(user_id: int) -> bool:
	"""
 	Check if the user is a tester.
 	"""
	try:
		connection = await get_conn()
		user = await db.get_user(connection, user_id)

		return user.is_test_active
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False


@logger.catch
async def is_tester_expired(user_id: int) -> bool:
	"""
	Check if the user's tester status has expired.
	"""
	current_time = datetime.now()
	try:
		connection = await get_conn()
		user = await db.get_user(connection, user_id)

		if user.test_begin_date is None:
			return False

		return Subscriptions.tester.term + user.test_begin_date > current_time
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False


