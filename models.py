from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class TeaSet(Base):
    __tablename__ = "tea_sets"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)