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



@logger.catch
async def fiats_symbols() -> dict:
	"""
	Retrieve a dictionary mapping fiat currencies to their corresponding symbols.

	Returns:
		dict: A dictionary mapping fiat currencies to symbols.
	"""
	symbols = dict()
	connection = await get_conn()

	records = await connection.fetch(f"""
		SELECT fiat, fiat_symbol
		FROM supported_banks;
	""")

	for record in records:
		fiat = record.get("fiat")
		symbol = record.get("fiat_symbol")

		if not symbols.get(fiat):
			symbols[fiat] = symbol

	return symbols		