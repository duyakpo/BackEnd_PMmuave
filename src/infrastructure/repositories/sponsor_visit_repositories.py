from infrastructure.databases.mssql import session
from infrastructure.models.sponsor_visit_model import SponsorVisitModel
from datetime import datetime

class SponsorVisitRepository:

    def create(self, data):
        if "visit_time" not in data or not data["visit_time"]:
            data["visit_time"] = datetime.utcnow()
        visit = SponsorVisitModel(**data)
        session.add(visit)
        session.commit()
        session.refresh(visit)
        return visit

    def list_all(self):
        return session.query(SponsorVisitModel).all()
