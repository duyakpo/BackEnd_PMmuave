from sqlalchemy import Column, Integer, String
from database import Base

class TicketType(Base):
    __tablename__ = "ticket_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    