# src/infrastructure/repositories/event_repository.py

from sqlalchemy.orm import Session
from typing import List, Optional
from src.infrastructure.models.event_model import Event
from src.infrastructure.models.sponsor_model import SponsorModel

class EventRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_all(self) -> List[Event]:
        return self.session.query(Event).all()

    def find_by_id(self, event_id: int) -> Optional[Event]:
        return self.session.query(Event).filter(Event.id == event_id).first()

    def create(self, event: Event) -> Event:
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event

    def update(self, event_id: int, data: dict) -> Optional[Event]:
        event = self.find_by_id(event_id)
        if event:
            for key, value in data.items():
                setattr(event, key, value)
            self.session.commit()
            self.session.refresh(event)
        return event

    def list_sponsors_for_event(self, event_id: int) -> List[SponsorModel]:
        return self.session.query(SponsorModel).filter(SponsorModel.event_id == event_id).all()
        
    def add_sponsor_to_event(self, sponsor: SponsorModel) -> SponsorModel:
        self.session.add(sponsor)
        self.session.commit()
        self.session.refresh(sponsor)
        return sponsor