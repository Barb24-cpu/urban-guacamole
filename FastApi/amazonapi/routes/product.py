from datetime import datetime, timezone
from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import Optional
from db import prisma
from auth import get_current_member

router = APIRouter()

class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    selling_price: float = 0.0
    buying_price: float = 0.0
    qty: int = 1

class UpdateProductSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    selling_price: Optional[float] = None
    buying_price: Optional[float] = None
    qty: Optional[int] = None

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_product(payload: ProductSchema):
    new_product = await prisma.product.create(data={
        "name": payload.name,
        "description": payload.description,
        "selling_price": payload.selling_price,
        "buying_price": payload.buying_price
    })
    return {"message": "New item added", "product": new_product}

@router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(product_id: str, payload: UpdateProductSchema):
    existing = await prisma.product.find_unique(where={
        "id": product_id
    })

    if not existing:
        raise HTTPException(status_code=404, detail="Product to update not found")

    update_data = payload.model_dump(exclude_unset=True) # remove null

    update_data['updated_at'] = datetime.now(timezone.utc)
    print(update_data)

    updated_product = await prisma.product.update(
        where={"id": product_id},
        data=update_data
    )
    return {"message": "Product updated", "product": updated_product}

@router.get("/{product_id}")
async def get_by_id(product_id: str):
    product = await prisma.product.find_unique(where={
        "id": product_id
    })

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

# Route to protect getting all products
@router.get("/")
async def get_all(current_member = Depends(get_current_member)):
    print(current_member)
    products = await prisma.product.find_many(include={"product_image": True})
    return products

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    product = await prisma.product.find_unique(
        where={
            "id": product_id
        },
        include={"product_image": True}
    )

    if not product:
        raise HTTPException(status_code=404, detail="Product to delete not found")

    await prisma.product.delete(where={"id": product_id})

    return {"message": "Product deleted"}