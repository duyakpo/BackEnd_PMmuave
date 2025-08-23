from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base

class SponsorModel(Base):
    __tablename__ = "sponsors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))