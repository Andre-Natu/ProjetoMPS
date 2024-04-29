from pydantic import BaseModel

class Statistics(BaseModel):
    access_num: int

    class Config:
        orm_mode = True