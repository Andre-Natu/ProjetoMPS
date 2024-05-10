from fastapi import APIRouter
from facade.system_facade import SystemFacade
from database import SessionLocal
from services.message_service import send_message

db = SessionLocal()

router = APIRouter()
facade = SystemFacade(db)

@router.get("/")
async def home():
    facade.update_access_num()
    return {"message": facade.generate_welcome_message()}

@router.get("/sms/{phone_number}/{message}")
async def home(phone_number: str, message: str):
    result_message = send_message(phone_number, message)
    return {"message": result_message}