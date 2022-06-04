from aiogram.dispatcher.filters.state import StatesGroup, State


class SetState(StatesGroup):
    title = State()
    image = State()
    description = State()
    price = State()