from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

calalog = KeyboardButton('Чайный Каталог')
sets = KeyboardButton('Чайные Сеты')
# b3 = KeyboardButton('Поделиться контактом', request_contact=True)
# b4 = KeyboardButton('Поделиться местоположением', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(calalog, sets)