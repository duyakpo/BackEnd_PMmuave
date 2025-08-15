from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
class SponsorEventModel(Base):
    __tablename__ = 'sponsor_events'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    sponsor_id = Column(Integer, ForeignKey('sponsors.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    booth_location = Column(String(255))