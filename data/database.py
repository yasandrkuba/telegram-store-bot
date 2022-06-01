from create_bot import bot
from data.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Product

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:' \
                          f'{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def sql_start():
#     global cur, base
#     base = lite.connect("tea-store.db")
#     cur = base.cursor()
#     if base:
#         print('Database connected!')
#     base.execute(
#         'CREATE TABLE IF NOT EXISTS menu (title TEXT PRIMARY KEY, img TEXT, description TEXT, price INTEGER)')
#     base.commit()
#
#
# async def add_sql_command(state):
#     async with state.proxy() as data:
#
#         cur.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
#         base.commit()

async def add_product(state):
    async with state.proxy() as data:
        new_product = Product(**data)
        session.add(new_product)
        session.commit()


async def sql_read(message):
    for product in session.query(Product).all():
        await bot.send_photo(message.from_user.id, product.image,
                             f"{product.title}\nОпсание: {product.description}\nЦена - {product.price}")
#
#
# async def sql_read(message):
#     for i in cur.execute("SELECT * FROM menu").fetchall():
#         await bot.send_photo(message.from_user.id, i[1], f'{i[0]}\nОписание: {i[2]}\nЦена {i[-1]}')
#
#
# async def get_menu_list():
#     return cur.execute("SELECT * FROM menu").fetchall()
#
#
# async def delete_command(data):
#     cur.execute("DELETE FROM menu WHERE title == ?", (data,))
#     base.commit()
