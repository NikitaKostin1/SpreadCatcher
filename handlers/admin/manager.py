from aiogram import types

from config import logger, get_conn
from create_bot import bot
from database import (
	admin as db,
	transaction as txn_db
)



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

