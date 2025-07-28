from fastapi import FastAPI
import uvicorn

app = FastAPI()

# product database
products_data = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Mouse", "price": 25.50}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the GET API - Fetch a product by ID"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = products_data.get(product_id)
    if product:
        return {"product_id": product_id, "data": product}
    return {"error": "Product not found"}

if __name__ == "__main__":
    uvicorn.run("get_example:app", host="127.0.0.1", port=8000, reload=True)