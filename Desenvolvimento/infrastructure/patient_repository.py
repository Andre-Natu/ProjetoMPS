from sqlalchemy.orm import Session
from models.models import Patient
from schemas.patient import PatientSchema
from business.patient_repository import PatientRepository
from validation import PatientValidation
from fastapi import HTTPException, status

class SQLAlchemyPatientRepository(PatientRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_patients(self):
        if len(self.db.query(Patient).all()) == 0:
            return {"Não existe usuário cadastrado"}
        return self.db.query(Patient).all()

    def create_patient(self, patient: PatientSchema):
        try:
            PatientValidation.validate_all(patient.username, patient.email, patient.password)

            new_patient = Patient(
                username=patient.username,
                email=patient.email,
                password=patient.password
            )

            self.db.add(new_patient)
            self.db.commit()

            return new_patient

        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
