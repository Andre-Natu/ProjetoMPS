from sqlalchemy.orm import Session
from infrastructure.statistics_repository import StatisticsRepository
from schemas.statistics import Statistics

class StatisticsRepository:
    def __init__(self, db: Session):
        self.statistics_repo = StatisticsRepository(db)

    def get_access_num(self) -> int:
        return self.statistics_repo.get_access_num()

    def update_access_num(self, new_access_num: int):
        self.statistics_repo.update_access_num(new_access_num)

    def create_stats(self, stats: Statistics) -> Statistics:
        return self.statistics_repo.create_stats(stats)
