from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from infrastructure.databases.base import Base

class TicketTypeModel(Base):
    __tablename__ = 'ticket_types'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)  # VIP, Standard, Free
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
