from aiogram.types import InlineKeyboardMarkup
from aiogram.types.input_file import InputFile

from config import logger
from create_bot import bot



@logger.catch
async def send_video(user_id: int|str, video: str|InputFile, caption: str=None, markup: InlineKeyboardMarkup=None):
	"""
	Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document).
	"""
	try:
		msg = await bot.send_video(user_id, video=video, caption=caption, reply_markup=markup)
		return msg
	except:
		if caption:
			msg = await bot.send_message(user_id, caption, reply_markup=markup)
			return msg



@logger.catch
async def send_photo(user_id: int|str, photo: str|InputFile, caption: str=None, markup: InlineKeyboardMarkup=None):
	"""
	Use this method to send photo files
	"""
	try:
		msg = await bot.send_photo(user_id, photo=photo, caption=caption, reply_markup=markup)
		return msg
	except:
		if caption:
			msg = await bot.send_message(user_id, caption, reply_markup=markup)
			return msg
