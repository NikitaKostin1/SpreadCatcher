from typing import Union
from dataclasses import dataclass
from datetime import datetime



@dataclass
class User:
	"""
	Dataclass that containes necessary data about user
	"""
	user_id: int
	username: str="None"
	entry_date: datetime=None
	is_bot_on: bool=False

	is_subscription_active: bool=False
	subscription_id: int=0
	subscription_begin_date: datetime=None

	is_test_active: bool=False
	test_begin_date: datetime=None

	# full_name: str=None
	# phone: str=None
	# email: str=None
	# register_date: datetime=None
