from infrastructure.patient_repository import SQLAlchemyPatientRepository
from infrastructure.statistics_repository import StatisticsRepository
from infrastructure.doctor_repository import SQLAlchemyDoctorRepository
from services.welcome_message_service import WelcomeMessageGenerator

class SystemFacade:
    def __init__(self, db):
        self.db = db
        self.patient_repository = SQLAlchemyPatientRepository(self.db)
        self.doctor_repository = SQLAlchemyDoctorRepository(self.db)
        self.statistics_repository = StatisticsRepository(self.db)
        self.welcome_message = WelcomeMessageGenerator()

    def get_patients(self):
        return self.patient_repository.get_patients()

    def create_patient(self, patient):
        return self.patient_repository.create_patient(patient)
    
    def get_doctors(self):
        return self.doctor_repository.get_doctors()
    
    def create_doctor(self, doctor):
        return self.doctor_repository.create_doctor(doctor)

    def get_access_num(self):
        return self.statistics_repository.get_access_num()

    def update_access_num(self):
        return self.statistics_repository.update_access_num()
    
    def create_stats(self, stats):
        return self.statistics_repository.create_stats(stats)
    
    def generate_welcome_message(self):
        return self.welcome_message.generate_welcome_message()
