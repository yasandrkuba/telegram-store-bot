from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from data.config import settings
from create_bot import dp

admins = settings.admins


class IsUser(BoundFilter):
    async def check(self, message: Message):
        return message.from_user.id not in admins