from config import logger
from handlers.user import manager
import asyncio

from typing import Tuple
from entities import (
	BinanceParser, HuobiParser,
	BybitParser, OkxParser
)




@logger.catch
async def server(wait_for: int):
	while True:
		await asyncio.sleep(wait_for)
		logger.success("Server ping")

		active_users = await manager.get_active_users()
		logger.info(f"Active users amount: {len(active_users)}")

		for user in active_users:
			user_id = user.user_id

			parametres = await manager.get_user_parametres(user_id)

			for currency in parametres.currencies.value:
				try:
					parser = OkxParser(
						fiat=parametres.fiat.value,
						currency=currency,
						banks=parametres.banks.value,
						limits=parametres.limits.value
					)
				except Exception as e:
					logger.error(f"Parser creating {user_id=}: {e}")
					continue

