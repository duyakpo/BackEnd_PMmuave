from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.default import db

Base = db.Model

class Checkin(Base):
    _tablename_ = "checkins"

    checkin_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    event_id = Column(Integer, ForeignKey("events.event_id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")
    event = relationship("Event")