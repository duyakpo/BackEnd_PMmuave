from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base
class SurveyModel(Base):
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
