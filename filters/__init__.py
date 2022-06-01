from aiogram import Dispatcher
from .is_admin import IsAdmin
from .is_client import IsClient


# def setup(dp: Dispatcher):
#     dp.filters_factory.bind(IsAdmin, event_handlers=[dp.message_handlers])
#     dp.filters_factory.bind(IsClient, event_handlers=[dp.message_handlers])
