from typing import Union
from dataclasses import dataclass
from datetime import datetime



@dataclass
class Signal:
	"""
	
	"""
	markets: tuple
	fiat: str
	currency: str
	# prices: tuple
	bid_price: float
	ask_price: float
	banks: tuple
	spread: float
	text: str
	# pointer: str
	# links: tuple
	bid_link: str
	ask_link: str
