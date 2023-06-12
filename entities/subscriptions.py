from datetime import datetime, timedelta
from dataclasses import dataclass, astuple
from typing import Union
from config import logger

# from assets.texts import user as txt



@dataclass(frozen=True, order=True)
class Subscription:
	"""
	Subscription representation
	"""
	subscription_id: int
	term: Union[timedelta, None]

	title: str
	description: str
	price: float

	is_full_access: bool
	is_multiple_activations: bool



@dataclass(frozen=True, order=True)
class Tester(Subscription):
	"""
	Has restrictions in product and can be activeted once
	"""
	subscription_id: int = 0
	term: Union[timedelta, None] = timedelta(hours=1)

	title: str = "Тестер"
	description: str = ""  # TODO: import from assets
	price: float = 0.00

	is_full_access: bool = False
	is_multiple_activations: bool = False



@dataclass(frozen=True, order=True)
class OneMonth(Subscription):
	"""
	Full access, multiple activations
	"""
	subscription_id: int = 1
	term: Union[timedelta, None] = timedelta(weeks=4)

	title: str = "1 месяц"
	description: str = ""  # TODO: import from assets
	price: float = 1299.00

	is_full_access: bool = True
	is_multiple_activations: bool = True



@dataclass(frozen=True, order=True)
class ThreeMonths(Subscription):
	"""
	Full access, multiple activations
	"""
	subscription_id: int = 2
	term: Union[timedelta, None] = timedelta(weeks=12)

	title: str = "3 месяца"
	description: str = ""  # TODO: import from assets
	price: float = 2490.00
	
	is_full_access: bool = True
	is_multiple_activations: bool = True



@dataclass(frozen=True, order=True)
class Unlimited(Subscription):
	"""
	Full access, one activation
	"""
	subscription_id: int = 3
	term: Union[timedelta, None] = None

	title: str = "Бессрочно"
	description: str = ""  # TODO: import from assets
	price: float = 9990.00
	
	is_full_access: bool = True
	is_multiple_activations: bool = False



@dataclass(frozen=True, order=True)
class Subscriptions:
	"""
	Containes available subscription
	"""
	tester: Subscription = Tester
	one_month: Subscription = OneMonth
	three_months: Subscription = ThreeMonths
	unlimited: Subscription = Unlimited


	@logger.catch
	def by_id(self, subscription_id: int|str) -> Subscription:
		"""
		Returns subscription by id
		in wrong id case return None
		"""
		for subscription in astuple(self):
			if int(subscription_id) == subscription.subscription_id:
				return subscription



Subscriptions = Subscriptions()
