from aiogram import types
from dataclasses import astuple

from config import logger, get_conn
from create_bot import bot
from database import (
	user as user_db,
	admin as db
)

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