from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base


class SponsorVisitModel(Base):
    __tablename__ = "sponsor_visits"
    id = Column(Integer, primary_key=True)
    sponsor_id = Column(Integer, ForeignKey("sponsors.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    visit_time = Column(DateTime)