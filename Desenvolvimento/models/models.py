from database import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

class Patient(Base):
    __tablename__ = 'patient'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(55), nullable=False)
    email: Mapped[str] = mapped_column(String(55), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(55), nullable=False, unique=False)

class Statistics(Base):
    __tablename__ = 'statistics'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    access_num: Mapped[int] = mapped_column(Integer,nullable=True, default=0)


