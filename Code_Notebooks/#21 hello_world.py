# import FastAPI
from fastapi import FastAPI

# import uvicorn to run the app
import uvicorn

# create FastAPI app instance 
app = FastAPI(
    title="My First API",                    # title shown in docs
    description="A simple API using FastAPI", # short description
    version="1.0.0"                          # version info
)

# define the route (homepage)
@app.get("/")  # this handle get request to "/"
def read_root():
    return {"message" : "Hello World! Welcome to FastAPI!"}  # JSON response

# define a route that takes a name from the URL
@app.get("/hello/{name}!")  # Handles GET requests 
def read_item(name: str):
    return {"message" : f"Hello, {name}!"}

if __name__ == "__main__":
    # start the server using uvicorn
    uvicorn.run("hello_world:app", host="127.0.0.1", port=8000, reload=True)