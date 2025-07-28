from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Simulated user data
users_data = {}

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the POST API - Create a new user"}

@app.post("/users/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in users_data:
        return {"error": "User already exists"}
    users_data[user_id] = user.dict()
    return {"message": "User created", "data": users_data[user_id]}

if __name__ == "__main__":
    uvicorn.run("post_example:app", host="127.0.0.1", port=8000, reload=True)
