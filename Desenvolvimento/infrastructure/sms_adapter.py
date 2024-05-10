from business.message_service import MessageService
from services.third_party_sms_service import ThirdPartySMSService

class SMSAdapter(MessageService):
    def __init__(self, third_party_service: ThirdPartySMSService):
        self.third_party_service = third_party_service

    def send_sms(self, phone_number: str, message: str):
        self.third_party_service.send_message(to=phone_number, message=message)
        return "Mensagem SMS enviada com sucesso para o número {}: {}".format(phone_number, message)
