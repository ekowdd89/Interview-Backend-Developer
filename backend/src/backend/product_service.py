from fastapi import Depends, HTTPException
from .schemas import ProductCreate, ProductRead, ProductUpdate
from .models import Product
from .product_repository import ProductRepository

from typing import List

class ProductService:
    productRepo: ProductRepository

    def __init__(self, productRepo: ProductRepository = Depends()):
        self.productRepo = productRepo
    def create_product(self, product: ProductCreate) -> Product:
        return self.productRepo.create_product(product)

    def get_all_products(self) -> List[ProductRead]:
        return self.productRepo.get_all_products()

    def get_product(self, product_id: int) -> Product:
        return self.productRepo.get_product(product_id)

    def update_product(self, product: ProductUpdate, product_id: int) -> Product:
        return self.productRepo.update_product(product, product_id)

    def delete_product(self, product_id) -> Product:
        return self.productRepo.delete_product(product_id)