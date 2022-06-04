from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

add_product = KeyboardButton('➕ Добавить товар')
cancel_adding = KeyboardButton('❌ Отменить добавление')
get_catalog = KeyboardButton('Посмотреть каталог')

add_set = KeyboardButton("➕ Добавить сет")
get_sets = KeyboardButton("Посмотреть сеты")

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(add_product, add_set).row(get_catalog, get_sets)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_adding)
kb_catalog = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(add_product)
kb_sets = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(add_set)