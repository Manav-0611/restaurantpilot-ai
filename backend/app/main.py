from fastapi import FastAPI

from app.core.config import APP_NAME, APP_VERSION
from app.db.database import engine
from app.db.base import Base

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    description="AI-powered restaurant operating system",
    version=APP_VERSION,
)

@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME} 🚀"
    }