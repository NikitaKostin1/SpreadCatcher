from asyncpg.connection import Connection
from datetime import datetime, timedelta
from typing import Union, Tuple
from config import logger, get_conn

from entities import (
	User
)
from entities.parametres import (
	Banks, Fiat
)




@logger.catch
async def get_banks_by_fiat(fiat: Fiat) -> Banks:
	"""
	Retrieve a list of banks that support the specified fiat currency.

	Args:
		fiat (str): The fiat currency.

	Returns:
		list: A list of banks that support the specified fiat currency.
	"""
	banks = Banks([])
	connection = await get_conn()

	records = await connection.fetch(f"""
		SELECT * 
		FROM supported_banks
		WHERE fiat = '{fiat.value.upper()}';
	""")

	for record in records:
		bank = record.get("bank")
		banks.value.append(bank)

	return banks