from fastapi import FastAPI
from pydantic import BaseModel
from schemas.patient import PatientSchema
from schemas.statistics import Statistics
from business.patient_repository import PatientRepository
from infrastructure.patient_repository import SQLAlchemyPatientRepository
from infrastructure.statistics_repository import StatisticsRepository
from create_report import create_report_txt
from services.services import send_sms
from database import SessionLocal, Base, engine

Base.metadata.create_all(engine)
db = SessionLocal()
patient_repository: PatientRepository = SQLAlchemyPatientRepository(db)
statistics_repository: StatisticsRepository = StatisticsRepository(db)

app = FastAPI()

@app.get("/")
async def home():
    statistics_repository.update_access_num()
    return {"message": "Bem-vindo ao sistema odontológico!"}

@app.get("/sms/{phone_number}/{message}")
async def home(phone_number: str, message: str):
    result_message = send_sms(phone_number, message)
    return {"message": result_message}

@app.get("/patients")
async def get_patients():
    return patient_repository.get_patients()

@app.get('/report')
async def create_report():
    return create_report_txt(statistics_repository)

@app.post("/patients/")
async def create_patient(patient: PatientSchema):
    return patient_repository.create_patient(patient)

@app.post("/create_stats")
async def create_stats(stats: Statistics):
    return statistics_repository.create_stats(stats)
