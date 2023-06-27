from dataclasses import dataclass



@dataclass
class AdvСonditions:
	"""Data class representing the conditions of an advertisement"""
	fiat: str
	currency: str
	price: float
	bank: tuple
	limits_min: int
	limits_max: int



@dataclass
class Advertiser:
	"""Data class representing an advertiser"""
	advertiser_id: int



@dataclass
class Advertisement:
	"""Data class representing an advertisement"""
	market: str
	conditions: AdvСonditions
	advertiser: Advertiser



@dataclass
class ParserResponse:
	"""Data class representing the response from the parser"""
	best_bid: 	Advertisement = None
	best_ask: 	Advertisement = None
	second_bid: Advertisement = None
	second_ask: Advertisement = None
