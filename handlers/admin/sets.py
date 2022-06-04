# from aiogram.dispatcher import FSMContext
# from aiogram import types
# from create_bot import bot, dp
# from keyboards import admin_kb
# from data.database import add_set
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from filters import IsAdmin
# from states import SetState
#
#
# @dp.message_handler(IsAdmin(), text="➕ Добавить сет", state=None)
# async def start_adding_set(message: types.Message):
#     await SetState.title.set()
#     await message.answer("Введи название", reply_markup=admin_kb.kb_cancel)
#
#
# @dp.message_handler(IsAdmin(), state=SetState.title)
# async def load_set_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['title'] = message.text
#         await SetState.next()
#         await message.answer("Теперь загрузи фото")
#
#
# @dp.message_handler(IsAdmin(), content_types=['photo'], state=FSMadmin.photo)
# async def load_set_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['image'] = message.photo[0].file_id
#         await SetState.next()
#         await message.answer("Теперь введи описание")
#
#
# @dp.message_handler(IsAdmin(), state=SetState.description)
# async def load_set_description(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['description'] = message.text
#         await SetState.next()
#         await message.answer("Теперь укажи цену")
#
#
# @dp.message_handler(IsAdmin(), state=SetState.price)
# async def load_set_price(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['price'] = int(message.text)
#     await add_set(state)
#     await message.answer("Сет успешно добавлен", reply_markup=admin_kb.kb_admin)
#     await state.finish()
#
#
# @dp.callback_query_handler(Text(startswith="del "))
# async def del_callback_run(callback: types.CallbackQuery):
#     await delete_product(callback.data.replace('del ', ''))
#     await callback.answer(text=f"{callback.data.replace('del ', '')} удалён.", show_alert=True)
#
#
# @dp.message_handler(IsAdmin(), text="Посмотреть каталог")
# async def get_catalog(message: types.Message):
#     queryset = await get_product_list()
#     for product in queryset:
#         await bot.send_photo(message.from_user.id, product.image,
#                              f"{product.title}\nОпсание: {product.description}\nЦена - {product.price}")
#         await bot.send_message(message.from_user.id, "⁠", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
#             f"Удалить {product.title}", callback_data=f"del {product.title}")))
