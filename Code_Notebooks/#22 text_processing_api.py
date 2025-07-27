from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

# creating FastAPI instance 
app = FastAPI(
    title="Simple Text API",
    description="A simple API for text processing",
    version="1.0.0"
)

# defining a Pydantic model for request body
class TextRequest(BaseModel):
    text: str
    uppercase: Optional[bool] = False

# defining a Pydantic model for the response
class TextResponse(BaseModel):
    processed_text: str
    text_length: int

# # defining a route (endpoint)
@app.get("/")
def read_root():
    return {"message" : "Welcome to our Text Processing API!"}

# defining a POST endpoint for text processing 
@app.post("/process-text/", response_model=TextResponse)
def process_text(request: TextRequest):
    # get the text from request 
    text = request.text

    # check if the the text is empty
    if not text:
        raise HTTPException(status_code=400, detail="Text can't be empty")
    
    # processing the text (convert to uppercase if requested) 
    processed_text = text.upper() if request.uppercase else text

    # creating response
    response = TextResponse(
        processed_text=processed_text,
        text_length=len(processed_text)
    )
    
    return response

if __name__ == "__main__":
    uvicorn.run("text_processing:app", host="127.0.0.1", port=8000, reload=True)