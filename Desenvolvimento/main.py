from fastapi import FastAPI
from pydantic import BaseModel
from schemas.user import UserSchema
from models.models import User
from controller.user import create_user_db, get_users_db
from database import SessionLocal, Base, engine

Base.metadata.create_all(engine)
db=SessionLocal()

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Bem-vindo ao sistema odontológico!"}

@app.get("/users")
async def get_users():
    return get_users_db()

@app.post("/users/")
async def create_user(user: UserSchema):
    return create_user_db(user)