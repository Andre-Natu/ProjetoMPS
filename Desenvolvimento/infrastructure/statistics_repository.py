from sqlalchemy.orm import Session
from models.models import Statistics

class StatisticsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_access_num(self) -> int:
        statistics = self.db.query(Statistics).first()
        if statistics:
            return statistics.access_num
        return 0

    def update_access_num(self):
        statistics = self.db.query(Statistics).first()
        if statistics:
            statistics.access_num += 1
            self.db.commit()
        return 0
    
    def create_stats(self, stats: Statistics):
        new_stats = Statistics(access_num=stats.access_num)
        self.db.add(new_stats)
        self.db.commit()
        
        return new_stats
