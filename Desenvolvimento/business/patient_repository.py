from abc import ABC, abstractmethod
from schemas.patient import PatientSchema

class PatientRepository(ABC):
    @abstractmethod
    def get_patients(self):
        pass
    
    @abstractmethod
    def create_patient(self, patient: PatientSchema):
        pass