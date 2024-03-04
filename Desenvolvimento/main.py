from fastapi import FastAPI
from pydantic import BaseModel
from schemas.user import UserSchema
from models.models import User
from controller.user import create_user_db, get_users_db

app = FastAPI()

banco = []

@app.get("/")
async def home():
    return {"message": "Bem-vindo ao sistema odontológico!"}

@app.get("/users")
async def get_users():
    return get_users_db(banco)

@app.post("/users/")
async def create_user(user: UserSchema):
    return create_user_db(user, banco)