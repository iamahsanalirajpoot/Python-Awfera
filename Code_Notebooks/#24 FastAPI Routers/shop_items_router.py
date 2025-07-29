from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

# Pydantic model for validation
class Product(BaseModel):
    name: str
    price: float

# Create router instance
router = APIRouter()

# fake items DB
items_db: Dict[int, Dict] = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Keyboard", "price": 49.99},
    3: {"name": "Mouse", "price": 19.99}
}

# GET all items
@router.get("/items")
def get_all_items():
    """
    Returns all available shop items with their count.
    """
    return {"total": len(items_db), "items": items_db}

# GET item by ID
@router.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Returns a single item based on its ID.
    """
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# POST add item
@router.post("/items/{item_id}")
def add_item(item_id: int, product: Product):
    """
    Adds a new item with the given ID.
    """
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items_db[item_id] = product.dict()
    return {"message": "Item added successfully", "item": items_db[item_id]}

# PUT update item
@router.put("/items/{item_id}")
def update_item(item_id: int, product: Product):
    """
    Updates an existing item by its ID.
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = product.dict()
    return {"message": "Item updated", "item": items_db[item_id]}

# DELETE item
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Deletes an item by its ID.
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "deleted_item": deleted_item}