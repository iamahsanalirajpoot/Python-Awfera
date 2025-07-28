from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Simulated user database
users_data = {
    1: {"name": "Ahsan", "age": 18},
    2: {"name": "Usman", "age": 21}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the DELETE API - Remove a user by ID"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users_data:
        deleted_user = users_data.pop(user_id)
        return {"message": "User deleted", "data": deleted_user}
    return {"error": "User not found"}

if __name__ == "__main__":
    uvicorn.run("delete_example:app", host="127.0.0.1", port=8000, reload=True)