from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('/Меню')
b2 = KeyboardButton('button 2')
# b3 = KeyboardButton('Поделиться контактом', request_contact=True)
# b4 = KeyboardButton('Поделиться местоположением', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).add(b2)