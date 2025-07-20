from fastapi import APIRouter, Depends, HTTPException
from typing import List
from .schemas import ProductCreate, ProductUpdate, ProductRead
from .product_service import ProductService

router = APIRouter()


@router.post("/products", response_model=ProductRead)
async def create_product(product: ProductCreate, service: ProductService = Depends()):
    return service.create_product(product)

@router.get("/products", response_model=List[ProductRead])
async def get_all_products(service: ProductService = Depends()):
    return service.get_all_products()
@router.get("/products/{product_id}", response_model=ProductRead)
async def get_product(product_id: int, service: ProductService = Depends()):
    return service.get_product(product_id)

@router.put("/products/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, product: ProductUpdate, service: ProductService = Depends()):
    return service.update_product(product, product_id)

@router.delete("/products/{product_id}", response_model=ProductRead)
async def delete_product(product_id: int, service: ProductService = Depends()):
    return service.delete_product(product_id)