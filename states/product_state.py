from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductState(StatesGroup):
    title = State()
    image = State()
    description = State()
    price = State()