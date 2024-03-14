from fastapi import HTTPException, status
from models.models import User
from schemas.user import UserSchema
from validation import UserValidation
import json

def get_users_db(db):
    users = db.query(User).all()
    return users

def create_user_db(user: UserSchema, db):
    try:
        UserValidation.validate_all(user.username, user.email, user.password)

        new_user = User(
            username=user.username,
            email=user.email,
            password=user.password
        )

        db.add(new_user)
        db.commit()

        return new_user

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))