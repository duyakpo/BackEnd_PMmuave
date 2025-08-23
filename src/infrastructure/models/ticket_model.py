from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from infrastructure.databases.base import Base

class TicketModel(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)  # VIP, Regular...
    status = Column(String, default="unpaid") 