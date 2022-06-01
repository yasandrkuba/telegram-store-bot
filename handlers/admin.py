from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import admin_kb
from data.database import add_product
# from data.database import add_sql_command, get_menu_list, delete_command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters import IsAdmin


class FSMadmin(StatesGroup):
    title = State()
    photo = State()
    description = State()
    price = State()


@dp.message_handler(is_admin=True, commands='start')
async def admin_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери действие", reply_markup=admin_kb.kb_admin)


@dp.message_handler(is_admin=True, commands="Загрузить", state=None)
@dp.message_handler(Text(endswith="Добавить товар", ignore_case=True))
async def cm_start(message: types.Message):
    await FSMadmin.title.set()
    await message.answer("Введи название", reply_markup=admin_kb.kb_cancel)


@dp.message_handler(Text(endswith="Отменить добавление", ignore_case=True), state='*')
@dp.message_handler(commands="отмена", state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Загрузка отменена", reply_markup=admin_kb.kb_admin)


@dp.message_handler(is_admin=True, state=FSMadmin.title)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
        await FSMadmin.next()
        await message.answer("Теперь загрузи фото")


@dp.message_handler(is_admin=True, content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['image'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.answer("Теперь введи описание")


@dp.message_handler(is_admin=True, state=FSMadmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await FSMadmin.next()
        await message.answer("Теперь укажи цену")


@dp.message_handler(is_admin=True, state=FSMadmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
    await add_product(state)
    await message.answer("Товар успешно добавлен")
    await state.finish()


# @dp.callback_query_handler(Text(startswith="del "))
# async def del_callback_run(callback: types.CallbackQuery):
#     await delete_command(callback.data.replace('del ', ''))
#     await callback.answer(text=f"{callback.data.replace('del ', '')} удалён.", show_alert=True)
#
#
# @dp.message_handler(Text(equals="удалить", ignore_case=True), is_admin=True)
# async def delete_item(message: types.Message):
#     queryset = await get_menu_list()
#     for q in queryset:
#         await bot.send_photo(message.from_user.id, q[1], f'{q[0]}\nОписание: {q[2]}\nЦена {q[-1]}')
#         await bot.send_message(message.from_user.id, "🗑", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
#             f"Удалить {q[0]}", callback_data=f"del {q[0]}")))


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=["Загрузить"], state=None)
    dp.register_message_handler(Text(equals="Загрузить", ignore_case=True))
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(cancel_handler, commands="отмена", state="*")
    dp.register_message_handler(load_name, state=FSMadmin.title)
    dp.register_message_handler(load_photo, state=FSMadmin.photo, content_types=['photo'])
    dp.register_message_handler(load_description, state=FSMadmin.description)
    dp.register_message_handler(load_price, state=FSMadmin.price)
