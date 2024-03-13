from fastapi import HTTPException, status
from models.models import User
from schemas.user import UserSchema
from validation import UserValidation
import json

def get_users_db():
    with open('banco.txt', 'r') as file:
        file = ''.join(file.readlines()).replace('"', '').strip()
        print(file)

    return 'Success ⭐️'

def create_user_db(user: UserSchema):
    try:
        UserValidation.validate_all(user.username, user.email, user.password)

        new_user = User(
            username=user.username,
            email=user.email,
            password=user.password
        )

        with open('banco.txt', 'a') as file:
            file.write(json.dumps(new_user.username) + '\n')
            file.write(json.dumps(new_user.email) + '\n')
            file.write(json.dumps(new_user.password) + '\n\n')

        return new_user

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))