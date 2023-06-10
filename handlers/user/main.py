from create_bot import Dispatcher
from aiogram import types
from config import logger

# from entities.states import Registration
# from entities import Courses
from . import (
	client
)



@logger.catch
def register_commands_handlers(dp: Dispatcher):
	"""
	Register all users commands
	"""
	# COMMANDS
	dp.register_message_handler(client.start, commands=["start"], state="*", chat_type=types.ChatType.PRIVATE)

	# # DATA SHARING
	# dp.register_message_handler(pre_access.info.give_access, content_types=types.ContentType.CONTACT)

	# # REPLY KEYBOARD
	# dp.register_message_handler(client.available_courses, lambda message: message.text == "Посмотреть курсы", state="*")
	# dp.register_message_handler(client.who_are_we, lambda message: message.text == "Кто мы?", state="*")
	# dp.register_message_handler(client.our_goals, lambda message: message.text == "Почему мы создали этот вебинар", state="*")
	# dp.register_message_handler(client.teachers, lambda message: message.text == "Преподаватели", state="*")
	# dp.register_message_handler(client.registration, lambda message: message.text == "Регистрация", state="*")
	# dp.register_message_handler(client.buy_subscription, lambda message: message.text == "Купить подписку", state="*")

	# # CALLBACKS
	# dp.register_callback_query_handler(pre_access.info.answer, lambda query: query.data and query.data == "start_info")

	# dp.register_callback_query_handler(courses.pages.turn_over, lambda query: query.data and query.data.split()[0] == "turn_over_course")

	# dp.register_callback_query_handler(payment.course_choice.options, lambda query: query.data and query.data.split()[0] == "course_choice")
	# dp.register_callback_query_handler(payment.course_choice.bought_course, lambda query: query.data and query.data == "bought_course")
	# dp.register_callback_query_handler(payment.type_choice.options, lambda query: query.data and query.data.split()[0] == "purchase")
	# dp.register_callback_query_handler(payment.types.instant.init_payment, lambda query: query.data and query.data.split()[0] == "payment_instant")
	

	# # STATES
	# dp.register_message_handler(registration.user_input.get_full_name, state=Registration.full_name)
	# dp.register_message_handler(registration.user_input.get_email, state=Registration.email)


