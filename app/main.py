from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.schema import User  # Make sure this matches your actual model import

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Social Escrow API!"}
