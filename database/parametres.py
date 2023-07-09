from config import logger, get_conn

from entities.parametres import (
	Banks, Fiat
)



@logger.catch
async def get_banks_by_fiat(fiat: Fiat) -> Banks:
	"""
	Retrieve a list of banks that support the specified fiat currency.

	Args:
		fiat (Fiat): The Fiat currency.

	Returns:
		Banks: A Banks object containing the list banks.
	"""
	banks = list()
	connection = await get_conn()

	records = await connection.fetch(f"""
		SELECT * 
		FROM supported_banks
		WHERE fiat = '{fiat.value.upper()}';
	""")

	for record in records:
		bank = record.get("bank")
		banks.append(bank)

	return Banks(banks)



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