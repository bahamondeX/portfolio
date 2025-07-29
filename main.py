# api/index.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

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

app.mount("/", StaticFiles(directory="dist", html=True), name="dist")

# You can add more FastAPI routes here
@app.get("/{path:path}")
async def serve_index(path: str):
    return FileResponse("dist/index.html")