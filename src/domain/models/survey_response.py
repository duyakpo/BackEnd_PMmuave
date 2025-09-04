from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.default import db

Base = db.Model

class SurveyResponse(Base):
    _tablename_ = "survey_responses"

    response_id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.survey_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    answer = Column(String)

    survey = relationship("Survey", back_populates="responses")
    user = relationship("User")