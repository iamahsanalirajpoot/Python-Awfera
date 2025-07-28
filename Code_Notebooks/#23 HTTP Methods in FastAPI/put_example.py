from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Simulated product database
products_data = {
    1: {"name": "Old Monitor", "price": 150.0}
}

class Product(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the PUT API - Update an existing product"}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in products_data:
        return {"error": "Product not found"}
    products_data[product_id] = product.dict()
    return {"message": "Product updated", "data": products_data[product_id]}

if __name__ == "__main__":
    uvicorn.run("put_example:app", host="127.0.0.1", port=8000, reload=True)
