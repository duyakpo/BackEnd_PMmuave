from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
class CheckinModel(Base):
    __tablename__ = "checkins"
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    checkin_time = Column(DateTime, nullable=False)