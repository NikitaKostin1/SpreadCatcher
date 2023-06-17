from aiogram.types import (
	InlineKeyboardMarkup, ReplyKeyboardMarkup,
	Message
)
from aiogram.types.input_file import InputFile
from datetime import datetime

from config import logger
from create_bot import bot
from . import manager

from keyboards.user import (
	reply as rkb
)



def date_to_int(date: datetime) -> int:
	year, month, day = date.year, date.month, date.day
	return ((year-1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400
			+ [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month - 1]
			+ day
			+ int(((year%4==0 and year%100!=0) or year%400==0) and month > 2))


@logger.catch
async def send_video( \
	user_id: int|str, video: str|InputFile, \
	caption: str=None, markup: InlineKeyboardMarkup=None) -> Message:
	"""
	Use this method to send video files, Telegram clients support mp4 videos 
	(other formats may be sent as Document).
	"""
	try:
		msg = await bot.send_video(
			user_id, video=video, caption=caption, reply_markup=markup
		)
		return msg
	except:
		if caption:
			msg = await bot.send_message(
				user_id, caption, reply_markup=markup,
				disable_web_page_preview=True
			)
			return msg


@logger.catch
async def send_photo( \
	user_id: int|str, photo: str|InputFile, \
	caption: str=None, markup: InlineKeyboardMarkup=None) -> Message:
	"""
	Use this method to send photo files
	"""
	try:
		msg = await bot.send_photo(
			user_id, photo=photo, caption=caption, reply_markup=markup
		)
		return msg
	except:
		if caption:
			msg = await bot.send_message(
				user_id, caption, reply_markup=markup,
				disable_web_page_preview=True
			)
			return msg


@logger.catch
async def determine_reply_markup(user_id: int) -> ReplyKeyboardMarkup:
	"""
	Determines the appropriate reply keyboard markup based on the user's status.
	"""
	if await manager.is_tester(user_id):
		return rkb.tester
	elif await manager.is_subscription_active(user_id):
		return rkb.active_subscription
	elif await manager.is_tester_expired(user_id):
		return rkb.tester_expired

	return rkb.new_user