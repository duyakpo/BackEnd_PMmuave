from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from infrastructure.databases.base import Base
class TicketTypeModel(Base):
    __tablename__ = "ticket_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
