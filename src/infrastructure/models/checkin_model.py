from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base

class CheckinModel(Base):
    __tablename__ = "checkins"
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    ticket = relationship("Ticket", back_populates="checkin")

    staff_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    staff = relationship("User", back_populates="checkins_made", foreign_keys=[staff_id])

    checkin_time = Column(DateTime, nullable=False)
