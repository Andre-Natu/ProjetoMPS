from sqlalchemy.orm import Session
from models.models import Doctor
from schemas.doctor import DoctorSchema
from business.doctor_repository import DoctorRepository
from validation import Validation
from fastapi import HTTPException, status

class SQLAlchemyDoctorRepository(DoctorRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_doctors(self):
        if len(self.db.query(Doctor).all()) == 0:
            return {"Não existe usuário cadastrado"}
        return self.db.query(Doctor).all()

    def create_doctor(self, doctor: DoctorSchema):
        try:
            Validation.validate_all(doctor.username, doctor.email, doctor.password)

            new_doctor = Doctor(
                username=doctor.username,
                email=doctor.email,
                password=doctor.password
            )

            self.db.add(new_doctor)
            self.db.commit()

            return new_doctor

        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
