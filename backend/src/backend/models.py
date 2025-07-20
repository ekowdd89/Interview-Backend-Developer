from sqlalchemy import Column, Integer, String, Float
from config.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    quantity = Column(Integer, index=True)