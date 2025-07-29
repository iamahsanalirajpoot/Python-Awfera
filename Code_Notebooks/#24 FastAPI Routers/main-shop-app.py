from fastapi import FastAPI
from shop_items_router import router as shop_router
import uvicorn 

# create the main shop (FastAPI Application)
app = FastAPI(title="Shop API")

# include the router 
app.include_router(shop_router, prefix="/shop", tags=["Shop Items"])

# Root route
@app.get("/")
def root():
    """
    Welcome message for the main shop entrance
    """
    return {"message": "Welcome to the Shop API!"}

@app.get("/about/")
def about_shop():
    """
    information about the shop.
    """
    return {"message" : "A simple shop API using FastAPI Routers"}

# Run the main shop
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
