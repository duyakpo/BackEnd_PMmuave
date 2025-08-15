from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base
class EventModel(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    event_type = Column(String(100), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    description = Column(Text)
    organizer_id = Column(Integer, ForeignKey("users.id"), nullable=False)