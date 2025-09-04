from src.domain.models.booth_visit import BoothVisit
from src.default import db

class BoothVisitRepository:
    def create(self,sponsor_id,user_id, event_id):
        visit = BoothVisit(sponsor_id=sponsor_id, user_id=user_id, event_id=event_id)
        db.session.add(visit)
        db.session.commit()
        return visit