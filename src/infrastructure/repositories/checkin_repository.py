from src.domain.models.checkin import Checkin
from src.default import db

class CheckinRepository:
    def create(self, user_id, event_id):
        checkin = Checkin(user_id=user_id, event_id=event_id)
        db.session.add(checkin)
        db.session.commit()
        return checkin