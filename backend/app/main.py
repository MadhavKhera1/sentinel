from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_TITLE", "Sentinel")
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Sentinel",
        "status": "Backend is running successfully"
    }
