from config import logger, get_conn

from datetime import datetime
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
		exists = await db.user_exists(connection, user_id)

		return exists
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False


# @logger.catch
# async def is_phone_entered(user_id: int) -> bool:
# 	"""
# 	Returns bool value if user has phone in db
# 	"""
# 	try:
# 		connection = await get_conn()
# 		entered = await db.phone_entered(connection, user_id)

# 		return entered
# 	except Exception as e:
# 		logger.error(f"{user_id}: {e}")
# 		return False



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


# @logger.catch
# async def new_user(user: User) -> bool:
# 	"""
# 	Inserts user's data in database
# 	Returns False in error case
# 	"""
# 	try:
# 		current_time = datetime.now()
# 		connection = await get_conn()
# 		registered = await db.new_user(connection, user, current_time)

# 		return registered
# 	except Exception as e:
# 		logger.error(f"{user}: {e}")
# 		return False


# @logger.catch
# async def is_registered(user_id: int) -> bool:
# 	"""
# 	returns bool value of users.registered column
# 	"""
# 	try:
# 		connection = await get_conn()
# 		registered = await db.is_registered(connection, user_id)

# 		return registered
# 	except Exception as e:
# 		logger.error(f"{user}: {e}")
# 		return False


# @logger.catch
# async def set_phone(user: User) -> bool:
# 	"""
# 	Inserts user's phone
# 	Returns False in error case
# 	"""
# 	try:
# 		connection = await get_conn()
# 		saved = await db.set_phone(connection, user)

# 		return saved
# 	except Exception as e:
# 		logger.error(f"{user}: {e}")
# 		return False


# @logger.catch
# async def registration(user: User) -> bool:
# 	"""
# 	Inserts user's registration data
# 	Returns False in error case
# 	"""
# 	try:
# 		current_time = datetime.now()
# 		connection = await get_conn()
# 		registered = await db.registration(connection, user, current_time)

# 		return registered
# 	except Exception as e:
# 		logger.error(f"{user}: {e}")
# 		return False


# @logger.catch
# async def save_purchase(purchase: Purchase) -> bool:
# 	"""
# 	Inserts purchase data
# 	Returns False in error case
# 	"""
# 	try:
# 		connection = await get_conn()
# 		saved = await db.save_purchase(connection, purchase)

# 		return saved
# 	except Exception as e:
# 		logger.error(f"{purchase}: {e}")
# 		return False


# @logger.catch
# async def get_purchases(user_id: int) -> Tuple[Purchase] | None:
# 	"""
# 	Returns tuple of Purchase objects that user has bought
# 	In error case return None
# 	"""
# 	try:
# 		connection = await get_conn()
# 		purchases = await db.get_purchases(connection, user_id)

# 		return purchases
# 	except Exception as e:
# 		logger.error(f"{user_id}: {e}")
# 		return None