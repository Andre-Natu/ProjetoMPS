from pydantic import BaseModel

class DoctorSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True