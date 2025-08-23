# src/infrastructure/repositories/event_repository.py
from infrastructure.models.event_model import EventModel
from infrastructure.databases.mssql import session

class EventRepository:
    def create(self, data):
        event = EventModel(**data)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

    def get_by_id(self, event_id):
        return session.query(EventModel).filter_by(id=event_id).first()

    def list_all(self):
        return session.query(EventModel).all()
