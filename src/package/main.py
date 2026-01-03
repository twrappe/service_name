"""
__SERVICE_NAME__ Microservice

Minimal FastAPI service skeleton with health check.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="__SERVICE_NAME__",
    description="Auto-generated microservice",
    version="0.1.0"
)

# Example data model
class Item(BaseModel):
    name: str
    value: int

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "__SERVICE_NAME__"}

# Example POST endpoint
@app.post("/items")
def create_item(item: Item):
    return {"message": "Item received", "item": item}

# Root endpoint
@app.get("/")
def root():
    return {"message": f"Welcome to the __SERVICE_NAME__ microservice!"}
