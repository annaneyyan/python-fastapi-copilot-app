from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model for POST request
class TextRequest(BaseModel):
    text: str

# Function to generate checksum
def generate(text: str):
    return hashlib.sha256(text.encode()).hexdigest()

# Welcome endpoint
@app.get("/")
def welcome():
    return {"message": "Welcome to the Token Generator API - Developed by Anna Tomy"}

# Existing endpoint
@app.get("/generate/{text}")
def generate_token(text: str):
    return {"text": text, "checksum": generate(text)}

# New POST endpoint
@app.post("/checksum")
def checksum(request: TextRequest):
    return {"text": request.text, "checksum": generate(request.text)}