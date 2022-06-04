from aiogram.dispatcher import FSMContext
from aiogram import types
from create_bot import bot, dp
from keyboards import admin_kb
from data.database import add_product, get_product_list, delete_product
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters import IsAdmin
from states import ProductState


@dp.message_handler(IsAdmin(), commands='start')
async def admin_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери действие", reply_markup=admin_kb.kb_admin)


@dp.message_handler(IsAdmin(), text="➕ Добавить товар", state=None)
async def start_adding_product(message: types.Message):
    await ProductState.title.set()
    await message.answer("Введи название", reply_markup=admin_kb.kb_cancel)


@dp.message_handler(IsAdmin(), text="❌ Отменить добавление", state='*')
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Добавление отменено")
    await state.finish()


@dp.message_handler(IsAdmin(), state=ProductState.title)
async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
        await message.answer("Теперь загрузи фото")
        await ProductState.next()


@dp.message_handler(IsAdmin(), content_types=['photo'], state=ProductState.image)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['image'] = message.photo[0].file_id
        await message.answer("Теперь введи описание")
        await ProductState.next()


@dp.message_handler(IsAdmin(), state=ProductState.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await message.answer("Теперь укажи цену")
        await ProductState.next()


@dp.message_handler(IsAdmin(), state=ProductState.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await add_product(state)
    await message.answer("Товар успешно добавлен", reply_markup=admin_kb.kb_admin)
    await state.finish()


@dp.callback_query_handler(text_startswith="del ")
async def del_callback_run(callback: types.CallbackQuery):
    await delete_product(callback.data.replace('del ', ''))
    await callback.answer(text=f"{callback.data.replace('del ', '')} удалён.", show_alert=True)


@dp.message_handler(IsAdmin(), text="Посмотреть каталог")
async def get_catalog(message: types.Message):
    queryset = await get_product_list()
    for product in queryset:
        await bot.send_photo(message.from_user.id, product.image,
                             f"{product.title}\nОпсание: {product.description}\nЦена - {product.price}")
        await bot.send_message(message.from_user.id, "⁠", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
            f"Удалить {product.title}", callback_data=f"del {product.title}")))
