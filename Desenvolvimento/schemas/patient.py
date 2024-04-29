from pydantic import BaseModel

class PatientSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True