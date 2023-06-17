from aiogram import types
from dataclasses import astuple
from typing import List

from config import logger, get_conn
from create_bot import bot
from database import admin as db

from entities import User



@logger.catch
async def get_admins() -> list:
	"""
	Return list of admins id
	"""
	try:
		connection = await get_conn()
		return await db.get_admins(connection)

	except Exception as e:
		logger.error(e)
		return []


@logger.catch
async def update_user(user: User) -> bool:
	"""
	Rewrite row in user table
	"""
	try:
		connection = await get_conn()
		success = await db.update_user(connection, user)

		return success
	except Exception as e:
		logger.error(f"{user.user_id}: {e}")
		return False


@logger.catch
async def reset_access(user_id: int) -> bool:
	"""
	Rewrite row in user table
	"""
	try:
		connection = await get_conn()
		success = await db.reset_access(connection, user_id)

		return success
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False


@logger.catch
async def get_tester_users() -> List[User]:
	"""
	Retrieves a list of users with active tester subscriptions.
	"""
	try:
		connection = await get_conn()
		users = await db.get_tester_users(connection)

		return users
	except Exception as e:
		logger.error(e)
		return list()


@logger.catch
async def set_tester_as_expired(user_id: int) -> bool:
	"""
	Sets the tester subscription as expired for a user.
	"""
	try:
		connection = await get_conn()
		user = await db.set_tester_as_expired(connection, user_id)

		return True
	except Exception as e:
		logger.error(f"{user_id}: {e}")
		return False