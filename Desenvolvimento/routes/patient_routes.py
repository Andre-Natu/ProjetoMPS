from fastapi import APIRouter
from schemas.patient import PatientSchema
from facade.system_facade import SystemFacade
from database import SessionLocal

db = SessionLocal()

router = APIRouter()
facade = SystemFacade(db)

@router.get("/patients")
async def get_patients():
    return facade.get_patients()

@router.post("/patients/")
async def create_patient(patient: PatientSchema):
    return facade.create_patient(patient)
