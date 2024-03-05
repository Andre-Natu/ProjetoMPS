from models.models import User
from schemas.user import UserSchema
import json

def get_users_db():
    with open('banco.txt', 'r') as file:
        file = ''.join(file.readlines()).replace('"', '').strip()
        print(file)

    return 'Success ⭐️'

def create_user_db(user: UserSchema):
    new_user=User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    with open('banco.txt', 'a') as file:
        file.write(json.dumps(new_user.username) + '\n')
        file.write(json.dumps(new_user.email) + '\n')
        file.write(json.dumps(new_user.password) + '\n\n')
    
    return new_user