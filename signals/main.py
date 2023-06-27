from config import logger
import threading
import asyncio

from . import thread



@logger.catch
def start_server():
	"""
	Starts the signals server in a separate thread.
	"""
	def asynchronous_start(wait_for=120):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)

		loop.run_until_complete(thread.server(wait_for))
		loop.close()

	server_thread = threading.Thread(
		target=asynchronous_start, args=(120,)
	)
	server_thread.daemon = True
	server_thread.start()