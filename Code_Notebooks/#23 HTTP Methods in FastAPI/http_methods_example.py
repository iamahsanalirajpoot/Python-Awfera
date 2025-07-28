from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI()

# Product model
class Product(BaseModel):
    name: str
    price: float

# product database
products_db: Dict[int, dict] = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Mouse", "price": 29.99},
    3: {"name": "Keyboard", "price": 49.99},
    4: {"name": "Monitor", "price": 199.99},
    5: {"name": "USB Drive", "price": 15.50}
}

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the HTTP Methods Example API"}

# GET
@app.get("/products")
def get_all_products():
    return {"total": len(products_db), "products": products_db}

# POST
@app.post("/products/{product_id}")
def create_product(product_id: int, product: Product):
    if product_id in products_db:
        return {"error": "Product already exists"}
    products_db[product_id] = product.dict()
    return {"message": "Product created", "data": product}

# PUT
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in products_db:
        return {"error": "Product not found"}
    products_db[product_id] = product.dict()
    return {"message": "Product updated", "data": product}

# DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id in products_db:
        deleted = products_db.pop(product_id)
        return {"message": "Product deleted", "data": deleted}
    return {"error": "Product not found"}

# run server
if __name__ == "__main__":
    uvicorn.run("http_methods_example:app", host="127.0.0.1", port=8000, reload=True)