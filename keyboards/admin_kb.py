from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_load = KeyboardButton('➕ Добавить товар')
button_delete = KeyboardButton('🗑 Удалить')
button_cancel = KeyboardButton('❌ Отменить добавление')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_load).add(button_delete)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_cancel)