from infrastructure.databases.mssql import session
from infrastructure.models.checkin_model import CheckInModel
from datetime import datetime

class CheckInRepository:
    def create(self, data):
        if not data.get("time"):
            data["time"] = datetime.utcnow()
        checkin = CheckInModel(**data)
        session.add(checkin)
        session.commit()
        session.refresh(checkin)
        return checkin

    def get_by_id(self, checkin_id):
        return session.query(CheckInModel).filter_by(id=checkin_id).first()

    def list_all(self):
        return session.query(CheckInModel).all()
