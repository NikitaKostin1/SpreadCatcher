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

	language: str="RU"
	first_visit: Union[str, datetime]=None
	is_admin: bool=False

	first_name: str=None
	full_name: str=None
	email: str=None
	phone: str=None


	# def __post_init__(self):
	# 	if isinstance(username, None):
	# 		self.username = "None"

