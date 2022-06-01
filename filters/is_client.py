from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS
from create_bot import dp


class IsClient(BoundFilter):
    key = "is_client"

    def __init__(self, is_client):
        self.is_admin = is_client

    async def check(self, message: Message):
        return message.from_user.id not in ADMINS


dp.filters_factory.bind(IsClient, event_handlers=[dp.message_handlers])
