from abc import ABC, abstractmethod

class MessageService(ABC):
    @abstractmethod
    def send_message(self, phone_number: str, message: str):
        pass