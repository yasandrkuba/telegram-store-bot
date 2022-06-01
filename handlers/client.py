from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from data.database import sql_read
from aiogram.dispatcher.filters import Text


# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Hi!\nIt's DenDaChaiBot!\nYou can order some tea here.",
                           reply_markup=kb_client)


async def menu_command(message: types.Message):
    await sql_read(message)


# @dp.message_handler()
async def echo_user(message: types.Message):
    await message.answer("Нет такой команды")
    await message.delete()


def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(menu_command, commands=["Меню"])
    dp.register_message_handler(menu_command, Text(equals="Меню", ignore_case=True))
    dp.register_message_handler(echo_user)
