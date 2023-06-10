from asyncpg.connection import Connection
from datetime import datetime
from typing import Tuple
from config import logger

from entities import User



@logger.catch
async def user_exists(connection: Connection, user_id: int) -> bool:
	"""
	Checks if user exists in database by chat_id
	"""
	record = await connection.fetchrow(f"SELECT * FROM users WHERE user_id = {user_id};")
	return bool(record)



# @logger.catch
# async def get_user(connection: Connection, user_id: int) -> User:
# 	"""
# 	Return User object from users
# 	In error case return None
# 	"""
# 	try:
# 		record = await connection.fetchrow(f"""
# 			SELECT * FROM users WHERE user_id = {user_id};
# 		""")
# 		if not record: return None

# 		user = User(
# 			user_id=record.get("user_id"),
# 			username=record.get("username"),
# 			first_visit=record.get("first_visit")
# 			# is_admin=record.get("is_admin")
# 		)

# 		return user
# 	except Exception as e:
# 		logger.error(f"{user_id}: {e}")
# 		return None


# @logger.catch
# async def new_user(connection: Connection, user: User, current_time: datetime) -> bool:
# 	"""
# 	Inserts new user into database
# 	"""
# 	try:
# 		# username column has VARCHAR(50) type
# 		if len(user.username) > 50:
# 			user.username = user.username[:50]

# 		await connection.execute(f"""
# 			BEGIN TRANSACTION ISOLATION LEVEL repeatable read;
# 			INSERT INTO users (user_id, username, first_visit) VALUES(
# 				{user.user_id}, '{user.username}', '{current_time}'
# 			);
# 			COMMIT;
# 		""")
		
# 		return True
# 	except Exception as e:
# 		logger.error(f"{user.user_id}: {e}")
# 		return False



# @logger.catch
# async def is_registered(connection: Connection, user_id: int) -> bool:
# 	"""
# 	returns bool value of users.registered column
# 	"""
# 	try:
# 		# BEGIN TRANSACTION ISOLATION LEVEL repeatable read;
# 		# COMMIT;
# 		record = await connection.fetchrow(f"""
# 			SELECT registered FROM users WHERE user_id = {user_id};
# 		""")

# 		return bool(record.get("registered"))
# 	except Exception as e:
# 		logger.error(f"{user_id}: {e}")
# 		return False



