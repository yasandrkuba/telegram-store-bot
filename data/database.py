from create_bot import bot
from data.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Product, TeaSet

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


async def add_product(state):
    async with state.proxy() as data:
        new_product = Product(**data)
        session.add(new_product)
        session.commit()


async def add_set(state):
    async with state.proxy() as data:
        new_set = TeaSet(**data)
        session.add(new_set)
        session.commit()


async def sql_read(message):
    for product in session.query(Product).all():
        await bot.send_photo(message.from_user.id, product.image,
                             f"{product.title}\nОпсание: {product.description}\nЦена - {product.price}")


async def get_product_list():
    query = session.query(Product).all()
    return query


async def delete_product(data):
    queryset = session.query(Product).filter(Product.title == data).first()
    session.delete(queryset)
    session.commit()
