from fastapi import APIRouter
from schemas.statistics import Statistics
from facade.system_facade import SystemFacade
from database import SessionLocal

db = SessionLocal()

router = APIRouter()
facade = SystemFacade(db)

@router.get("/statistics")
async def get_statistics():
    return {"access_num": facade.get_access_num()}

@router.post("/statistics")
async def create_statistics(stats: Statistics):
    return facade.create_stats(stats)