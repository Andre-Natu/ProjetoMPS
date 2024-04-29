from infrastructure.sms_adapter import SMSAdapter
from services.third_party_sms_service import ThirdPartySMSService

def send_sms(phone_number: str, message: str) -> str:
    # Criando uma instância do serviço de SMS externo
    third_party_service = ThirdPartySMSService()

    # Criando uma instância do adaptador SMS e passando o serviço de SMS externo como argumento
    sms_adapter = SMSAdapter(third_party_service)

    # Enviando a mensagem SMS
    return sms_adapter.send_message(phone_number=phone_number, message=message)
