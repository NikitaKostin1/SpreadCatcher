from config import logger
import json
import asyncio
import aiohttp

from .parser import (
	Parser, ParserResponse, Advertisement,
	Advertiser, AdvСonditions
) 

from aiohttp.client import ClientSession
from typing import (
	NoReturn, Union, Tuple
)



class PexpayParser(Parser):
	banks_alias = {
			"RaiffeisenBank": "RaiffeisenBankRussia",
			"Tinkoff": "Tinkoff",
			"Payeer": "Payeer",
			"QIWI": "QIWI",
			"AdvCash": "Advcash",
			"SBP": "SBP",
			"YandexMoney": "YandexMoney",
			"Sberbank": "Sberbank",
			"Alfa-bank": "AlfaBank"
		}

	@logger.catch
	def _adv_validation(self, response: dict, adv_type: Union["bid", "ask"], bank: str) -> Tuple[AdvСonditions, Advertiser]:
		"""
		Perform validation on each advertisement in the response and return conditions and advertiser data if valid.
		"""
		for advertisement_ndx in range(len(response)):
			advertisement = response[advertisement_ndx]

			# Extract advertisement data from the response
			price = float(advertisement["adDetailResp"]["price"])
			advertiser_advertisements_amount = advertisement["advertiserVo"]["userStatsRet"]["completedOrderNum"]
			advertiser_finish_rate = float(advertisement["advertiserVo"]["userStatsRet"]["finishRate"]) * 100
			total_adv_amount = len(response)

			# Check price difference and advertiser validation criteria
			if advertisement_ndx != total_adv_amount - 1 and total_adv_amount > 7:
				next_advertisement = response[advertisement_ndx+1]
				next_price = next_advertisement["adDetailResp"]["price"]

				if not self.price_difference_validation(
							advertisement_ndx, adv_type,
							price, next_price, total_adv_amount):
					continue

			if not self.advertiser_validation(
						advertiser_advertisements_amount,
						advertiser_finish_rate):
				continue

			conditions = AdvСonditions(
				fiat=self.fiat,
				currency=self.currency,
				price=float(advertisement["adDetailResp"]["price"]),
				bank=bank,
				limits_min=int(float(advertisement["adDetailResp"]["minSingleTransAmount"])),
				limits_max=int(float(advertisement["adDetailResp"]["maxSingleTransAmount"]))
			)
			advertiser = Advertiser(
				advertiser_id=advertisement["advertiserVo"]["userNo"]
			)

			advertisement = Advertisement(
				market="PexPay",
				conditions=conditions,
				advertiser=advertiser
			)

			# Determine the position of the advertisement in the list
			self.determine_adv_position(
				advertisement, adv_type
			)
			
		else:
			# No advertimsements
			return None


	@logger.catch
	async def _get_advertisements(self, adv_type: Union["bid", "ask"], bank: str, session: ClientSession) -> NoReturn:
		"""
		Fetch advertisements for the given advertisement type and bank using the PexPay.
		"""
		if bank not in PexpayParser.banks_alias:
			return

		parametres_format = {
			"bid": "BUY",
			"ask": "SELL"
		}
		parametres_json = {
			"page": 1,
			"rows": 10,
			"tradeType": parametres_format[adv_type],
			"asset": self.currency,
			"transAmount": str(self.limits),
			"fiat": self.fiat,
			"payTypes": [PexpayParser.banks_alias[bank]],
			"merchantCheck": False,
			"classifies": [],
			"filter": {
				"payTypes": []
			}
		}

		url = f"https://www.pexpay.com/bapi/c2c/v1/friendly/c2c/ad/search"

		async with session.post(
			url, headers={"Content-Type": "application/json"},
			data=json.dumps(parametres_json)
		) as client_response:
			try:
				response = json.loads(await client_response.text())
				if int(response["code"]) != 0:
					return
				if not response["data"]:
					# logger.warning(f"PexPay {adv_type} 0 adverstisments: {self.currency=}, {self.fiat=}, {bank=}, {self.limits=}")
					return
			except Exception as e:
				logger.error(f"PexPay parser: {e}")
				return

		self._adv_validation(response["data"], adv_type, bank)