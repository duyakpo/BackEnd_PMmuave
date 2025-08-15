from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base
class SurveyModel(Base):
    __tablename__ = 'surveys'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)

