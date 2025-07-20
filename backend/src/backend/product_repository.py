from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, lazyload
from config.database import get_db

from .models import Product
from .schemas import ProductCreate, ProductRead, ProductUpdate
class ProductRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all_products(self) -> List[ProductRead]:
        products = self.db.query(Product).all()
        response = [
            ProductRead.model_validate(product) for product in products
        ]
        print(response)
        return response
    def create_product(self, product: ProductCreate) -> ProductRead:
        crt_product = Product(
            name=product.name,
            price=product.price,
            quantity=product.quantity
        )
        self.db.add(crt_product)
        self.db.commit()
        self.db.refresh(crt_product)
        return ProductRead.model_validate(crt_product)
    def update_product(self, product: ProductUpdate, product_id: int) -> ProductRead:
        _product = self.db.query(Product).filter(Product.id == product_id).first()
        if  product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        if product.name is not None:
            _product.name = product.name
        if product.price is not None:
            _product.price = product.price
        if product.quantity is not None:
            _product.quantity = product.quantity
        self.db.merge(_product)
        self.db.commit()
        self.db.refresh(_product)
        response = ProductRead.model_validate(_product)
        return response
    def delete_product(self, product_id: int) -> ProductRead:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        self.db.delete(product)
        self.db.commit()
        self.db.refresh(product)
        response = ProductRead.model_validate(product)
        return response

    def get_product(self, product_id: int) -> ProductRead:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        response = ProductRead.model_validate(product)
        return response