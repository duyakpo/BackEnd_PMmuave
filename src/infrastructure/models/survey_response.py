from sqlalchemy import Column, Integer, String, Datatime, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.databases.base import Base
import datatime

class SurveyResponse(Base):
    __tablename__ = "survey_responses"
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    user_id = Column(Integer, nullable=False)
    answer = Column(String, nullable=False)
    submitted_at = Column(Datetime, default=datetime.datetime.utcnow)
    survey = relationship("Survey", back_populates="responses")
