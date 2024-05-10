# Classe que utiliza padrao singleton 
# Usamos essa classe na main

import random

class WelcomeMessageGenerator:
    _instance = None
    _welcome_messages = [
        "Bem-vindo!",
        "Olá, seja bem-vindo!",
        "Que bom ter você aqui!",
        "Seja bem-vindo à nossa aplicação!",
        "Olá, é um prazer tê-lo conosco!"
    ]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate_welcome_message(self):
        return random.choice(self._welcome_messages)
