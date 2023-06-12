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
	# TODO: check NOT NULL columns
	try:
		# for param in astuple(user):
		# 	if param is None:
		# 		logger.error(""" \
		# 			All parametres in the User instance must be provided!
		# 		""")
		# 		return False

		connection = await get_conn()
		success = await db.update_user(connection, user)

		return success
	except Exception as e:
		logger.error(f"{user.user_id}: {e}")
		return False