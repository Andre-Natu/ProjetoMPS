from models.models import User
from schemas.user import UserSchema
import json

def get_users_db(banco):
    return banco

def create_user_db(user: UserSchema, banco):
    pass