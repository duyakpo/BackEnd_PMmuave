from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
class TicketModel(Base):
    __tablename__ = 'tickets'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    ticket_type_id = Column(Integer, ForeignKey('ticket_types.id'), nullable=False)
    status = Column(String(50), nullable=False)  # paid, pending, canceled
    created_at = Column(DateTime)
