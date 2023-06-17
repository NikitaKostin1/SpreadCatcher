from asyncpg.connection import Connection
from entities import User

from config import logger



@logger.catch
async def get_admins(connection: Connection) -> list:
	"""
	Retrieves a list of admin IDs from the database.
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


@logger.catch
async def update_user(connection: Connection, user: User) -> bool:
	"""
	Updates a user's row in the user table.
	"""
	try:
		await connection.execute(f"""
			BEGIN TRANSACTION ISOLATION LEVEL repeatable read;

			UPDATE users 
			SET 
				user_id = {user.user_id},
				username = '{user.username}',
				entry_date = '{user.entry_date}',
				is_subscription_active = {user.is_subscription_active},
				subscription_id = {
					f'{user.subscription_id}' 
					if user.subscription_id or user.subscription_id == 0
					else 'NULL'
				},
				subscription_begin_date = {
					f"'{user.subscription_begin_date}'"
					if user.subscription_begin_date 
					else 'NULL'
				},
				is_test_active = {user.is_test_active},
				test_begin_date = {
					f"'{user.test_begin_date}'"
					if user.test_begin_date 
					else 'NULL'
				}
			WHERE user_id = {user.user_id};

			COMMIT;
		""")

		return True
	except Exception as e:
		logger.error(f"{user.user_id}: {e}")
		return False