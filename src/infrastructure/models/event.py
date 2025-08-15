from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from infrastructure.databases.base import Base
class EventModel(Base):
    __tablename__ = 'events'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String(255))
    created_by = Column(Integer, ForeignKey('users.id'))  # Người tạo sự kiện
    created_at = Column(DateTime)
    updated_at = Column(DateTime)