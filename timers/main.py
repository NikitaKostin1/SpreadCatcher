from aiogram import types
from config import logger
import asyncio

from . import subscriptions



loop = asyncio.get_event_loop()

@logger.catch
def register_timers():
	"""
	Register all timers
	"""
	loop.create_task(subscriptions.tester(wait_for=600))
	
	
