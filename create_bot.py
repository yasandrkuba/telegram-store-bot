from aiogram import Bot, Dispatcher
from data.config import settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

API_TOKEN = settings.secret_key

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
