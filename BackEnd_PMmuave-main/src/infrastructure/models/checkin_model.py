from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class CheckIn(Base):
    __tablename__ = "checkins"

    checkin_id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.ticket_id"))
    checkin_time = Column(DateTime)

    ticket = relationship("Ticket")
