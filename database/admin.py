from asyncpg.connection import Connection
from entities import User

from config import logger



@logger.catch
async def get_admins(connection: Connection) -> list:
	"""
	Return list of admins id
	"""
	admins = []
	try:
		records = await connection.fetch(f"""
			SELECT user_id FROM users WHERE is_admin = true;
		""")
		if not records:
			return []

		for records in records:
			admins.append(records.get("user_id"))

		return admins
	except Exception as e:
		logger.error(e)
		return []

