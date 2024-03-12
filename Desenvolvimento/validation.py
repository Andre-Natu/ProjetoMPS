from fastapi import HTTPException, status
import re

class UserValidation:
    @staticmethod
    def validate_username(username):
        if len(username) > 12:
            raise ValueError("O nome de usuário deve ter no máximo 12 caracteres.")
        if len(username) == 0:
            raise ValueError("O nome de usuário não pode ser vazio.")
        if bool(re.search(r'\d', username)):
            raise ValueError("O nome de usuário não pode ter números.")

    @staticmethod
    def validate_email(email):
        pass        

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("A senha deve ter no mínimo 8 caracteres.")
        if len(password) > 20:
            raise ValueError("A senha deve ter no máximo 20 caracteres.")
        if not re.search(r'[a-zA-Z]', password):
            raise ValueError("A senha deve conter letras.")
        if not re.search(r'\d.*\d', password):
            raise ValueError("A senha deve conter pelo menos dois números.")
    
    @staticmethod
    def validate_all(username, email, password):
        UserValidation.validate_username(username)
        UserValidation.validate_email(email)
        UserValidation.validate_password(password)
        