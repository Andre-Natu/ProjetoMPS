from abc import ABC, abstractmethod
from schemas.doctor import DoctorSchema

class DoctorRepository(ABC):
    @abstractmethod
    def get_doctors(self):
        pass
    
    @abstractmethod
    def create_doctor(self, patient: DoctorSchema):
        pass