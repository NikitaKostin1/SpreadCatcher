from aiogram.types.input_media import InputMedia
from aiogram.types.input_file import InputFile
from aiogram import types
from typing import Dict

from create_bot import bot
from config import logger



class MessageHandler:
	"""
	Messages pool to handle inline markup
	or to edit an old message
	"""
	def __init__(self):
		self.storage: Dict[int, types.Message] = {}


	@logger.catch
	async def acquire(self, message: types.Message) -> None:
		"""
		Rewrite message in storage 
		or set new message.
		If in storage was message, inline markup deletes
		"""
		if not message:
			return None

		USER_ID = message["chat"]["id"]

		if USER_ID in self.storage:
			await self.edit(USER_ID)

		self.storage[USER_ID] = message


	@logger.catch
	async def release(self, USER_ID: int) -> types.Message:
		"""
		Deletes message from storage by user_id
		Returns rewritten message: types.Message
		"""
		if not USER_ID in self.storage:
			return
		if not self.storage[USER_ID]:
			return

		message = self.storage[USER_ID]
		self.storage[USER_ID] = None
		message_id = message["message_id"]

		if "text" in message:
			text = message["text"]
		else:
			text = message["caption"]

		try:
			await bot.edit_message_text(
				chat_id=USER_ID,
				message_id=message_id,
				text=text,
				reply_markup=None,
				disable_web_page_preview=True
			)
		except:
			pass

		return message



	@logger.catch
	async def edit(self, USER_ID: int, text: str=None, markup: types.InlineKeyboardMarkup=None) -> bool:
		"""
		Edit message from storage
		Return bool value of operation
		"""
		if not USER_ID in self.storage:
			return False
		if not self.storage[USER_ID]:
			return False			

		message = self.storage[USER_ID]	
		message_id = message["message_id"]

		if not text:
			if "text" in message:
				text = message["text"]
			else:
				text = message["caption"]

		try:
			await bot.edit_message_text(
				chat_id=USER_ID,
				message_id=message_id,
				text=text,
				reply_markup=markup,
				disable_web_page_preview=True
			)
			return True
		except:
			return False


	@logger.catch
	async def delete(self, USER_ID: int) -> None:
		"""
		Deletes message from chat
		(Remains in storage)
		"""
		if not USER_ID in self.storage:
			return
		if not self.storage[USER_ID]:
			return False	

		message = await self.release(USER_ID)

		try:
			await message.delete()
		except:
			pass
		


	@logger.catch
	async def edit_media(self, USER_ID: int, media: InputMedia) -> bool:
		"""
		Use this method to edit animation, audio, document, photo, or video messages. 
		If a message is part of a message album, then it can be edited only to an audio for audio albums, 
		only to a document for document albums and to a photo or a video otherwise.
		Media's caption removes.

		https://docs.aiogram.dev/en/dev-3.x/api/methods/edit_message_media.html
		"""
		if not USER_ID in self.storage:
			return
		if not self.storage[USER_ID]:
			return False

		message = self.storage[USER_ID]	
		# message_id = message["message_id"]

		try:
			await message.edit_media(
					media=media
				)
			return True
		except:
			return False




MainMessage = MessageHandler()
AdditionalMessage = MessageHandler()