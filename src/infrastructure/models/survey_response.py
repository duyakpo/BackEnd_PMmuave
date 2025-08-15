from sqlalchemy import Column, Integer, String, Datatime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class SurveyResponse(Base):
    __tablename__ = "survey_responses"
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=False)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    survey = relationship("Survey", back_populates="responses")
   