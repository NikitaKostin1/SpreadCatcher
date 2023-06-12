from config import logger, get_conn

from datetime import datetime, timedelta
from typing import Tuple

from entities import User
from database import user as db





@logger.catch
async def is_user_exists(user_id: int) -> bool:
	"""
	Returns bool value if user exists in users table
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
	Return User object from users
	In error case return None
	"""
	try:
		connection = await get_conn()
		user = await db.get_user(connection, user_id)

		return user
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return None


@logger.catch
async def set_new_user(user: User) -> bool:
	"""
	Inserts user's data in database
	Returns False in error case
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
async def is_subscription_active(user_id: int) -> bool:
	"""
	# TODO: Specify minimum subscription_level
	returns bool value of users.subscription_level > 1
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
 	returns bool value of users.is_test_active column
 	"""
	try:
		connection = await get_conn()
		user = await db.get_user(connection, user_id)

		return user.is_test_active
	except Exception as e:
		logger.error(f"{user}: {e}")
		return False



@logger.catch
async def is_tester_expired(user_id: int) -> bool:
	"""
	returns bool value of users.is_test_active column
	"""
	current_time = datetime.now()
	try:
		connection = await get_conn()
		user = await db.get_user(connection, user_id)

		if user.test_begin_date is None:
			return False

 		# TODO: Specify hours amount source
		return timedelta(hours=1) + user.test_begin_date > current_time
	except Exception as e:
		logger.error(f"{user}: {e}")
		return False
