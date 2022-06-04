from aiogram import types
from create_bot import bot, dp
from keyboards import kb_client
from data.database import get_product_list


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Hi!\nIt's DenDaChaiBot!\nYou can order some tea here.",
                           reply_markup=kb_client)


@dp.message_handler(text_contains='Каталог')
async def get_catalog(message: types.Message):
    print(12312321123123)
    queryset = await get_product_list()
    for product in queryset:
        await bot.send_photo(message.from_user.id, product.image,
                             f"{product.title}\nОпсание: {product.description}\nЦена - {product.price}")


# @dp.message_handler()
# async def echo_user(message: types.Message):
#     await message.answer("Нет такой команды")
#     await message.delete()


# def register_client_handler(dp: Dispatcher):
#     dp.register_message_handler(send_welcome, commands=['start', 'help'])
#     dp.register_message_handler(get_menu, Text(endswith="Каталог", ignore_case=True), commands=["Меню"])
#     dp.register_message_handler(echo_user)
