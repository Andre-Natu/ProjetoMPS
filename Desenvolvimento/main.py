from fastapi import FastAPI
from routes.doctor_routes import router as doctor_router
from routes.patient_routes import router as patient_router
from routes.statistic_routes import router as statistics_router
from routes.general_routes import router as general_router

from database import Base, engine

Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(statistics_router)
app.include_router(general_router)


