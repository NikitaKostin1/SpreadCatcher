from create_bot import bot
from config import logger
import asyncio
import time

from handlers.user import manager as user_manager
from . import manager

from typing import List, Tuple, Dict
from entities.parsing.types import (
	ParserResponse, Advertisement
)
from entities import (
	User, Parametres, Signal
)


# Dict with the tuple of signals sent to a user
signals: Dict[int, Tuple[Signal]] = {}

@logger.catch
async def server(wait_for: int):
	"""
	Server function that runs periodically to process signals for active users

	Args:
		wait_for (int): The time interval to wait between server pings
	"""

	# List of user IDs that have been notified about inefficient parameters
	notificated_users: List[int] = list()
	min_acceptable_signals_amount = 5

	await manager.set_fiats_symbols()

	while True:
		await asyncio.sleep(10)
		logger.success("Server ping")

		active_users: List[User] = await user_manager.get_active_users()
		logger.info(f"Active users amount: {len(active_users)}")

		# Check if notified users turned off the bot
		for user_id in notificated_users:
			if not user_id in [user.user_id for user in active_users]:
				notificated_users.remove(user_id)

		for user in active_users:
			user_id = user.user_id

			parametres: Parametres = await user_manager.get_user_parametres(user_id)

			if not parametres:
				logger.error(f"No parametres: {user_id}")
				continue

			user_sent_signals = 0
			if signals.get(user_id):
				former_signals = signals[user_id]
			else:
				former_signals = tuple()

			for currency in parametres.currencies.value:
				parsers_responses = await manager.gather_parsers_responses(
					currency, parametres
				)

				sent_signals: Tuple[Signal] = await manager.iterate_advertisments(
					user_id, parametres, parsers_responses, former_signals
				)
				user_sent_signals += len(sent_signals)

			# Notification about inefficient parametres
			if user_sent_signals < min_acceptable_signals_amount and \
								not user_id in notificated_users:
				await manager.notificate_user(user_id)
				notificated_users.append(user_id)

			signals[user_id] = sent_signals
