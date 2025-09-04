from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.default import db

Base = db.Model

class BoothVisit(Base):
    _tablename_ = "booth_visits"

    visit_id = Column(Integer, primary_key=True, index=True)
    sponsor_id = Column(Integer, ForeignKey("sponsors.sponsor_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    event_id = Column(Integer, ForeignKey("events.event_id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    sponsor = relationship("Sponsor")
    user = relationship("User")
    event = relationship("Event")