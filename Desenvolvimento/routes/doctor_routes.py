from fastapi import APIRouter   
from schemas.doctor import DoctorSchema
from facade.system_facade import SystemFacade
from database import SessionLocal

db = SessionLocal()

router = APIRouter()
facade = SystemFacade(db)

@router.get("/doctors")
async def get_doctors():
    return facade.get_doctors()

@router.post("/doctors/")
async def create_doctor(doctor: DoctorSchema):
    return facade.create_doctor(doctor)
