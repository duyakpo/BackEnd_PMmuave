# src/infrastructure/repositories/ticket_type_repository.py

from sqlalchemy.orm import Session
from typing import List, Optional
from src.infrastructure.models.ticket_type_model import TicketTypeModel

class TicketTypeRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_for_event(self, event_id: int) -> List[TicketTypeModel]:
        return self.session.query(TicketTypeModel).filter(TicketTypeModel.event_id == event_id).all()

    def add_to_event(self, ticket_type: TicketTypeModel) -> TicketTypeModel:
        self.session.add(ticket_type)
        self.session.commit()
        self.session.refresh(ticket_type)
        return ticket_type
        
    def update(self, type_id: int, data: dict) -> Optional[TicketTypeModel]:
        ticket_type = self.session.query(TicketTypeModel).filter(TicketTypeModel.id == type_id).first()
        if ticket_type:
            for key, value in data.items():
                setattr(ticket_type, key, value)
            self.session.commit()
            self.session.refresh(ticket_type)
        return ticket_type