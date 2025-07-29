# api/index.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configure CORS to allow requests from your frontend domain
# In a production environment, replace "*" with your actual frontend domain(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/api/hello")
def read_root():
    """
    A simple GET endpoint that returns a greeting.
    """
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: str|None=None):
    """
    An example endpoint with path and query parameters.
    """
    return {"item_id": item_id, "q": q}

# You can add more FastAPI routes here