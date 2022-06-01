from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
# from data.config import ADMINS
from create_bot import dp
from data.config import settings

admins = settings.admins


class IsAdmin(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: Message):
        return message.from_user.id in admins


dp.filters_factory.bind(IsAdmin, event_handlers=[dp.message_handlers])
