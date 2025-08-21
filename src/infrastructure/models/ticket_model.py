from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base

class TicketModel(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    ticket_type_id = Column(Integer, ForeignKey("ticket_types.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    status = Column(String(50), nullable=False)
    qr_code = Column(String(255))
