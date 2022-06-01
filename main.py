import logging
from create_bot import dp
from handlers import client, admin
from aiogram import executor
import models
from data import database

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    print("Bot is online...")
    models.Base.metadata.create_all(bind=database.engine)
    # db.sql_start()


client.register_client_handler(dp)
admin.register_admin_handler(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
