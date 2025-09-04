from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.default import db

Base = db.Model

class Survey(Base):
    _tablename_ = "surveys"

    survey_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.event_id"))
    title = Column(String, nullable=False)

    event = relationship("Event")
    responses = relationship("SurveyResponse", back_populates="survey")