from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Checkin(Base):
    __tablename__ = "checkins"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    event_id = Column(String, nullable=False)

class BoothVisit(Base):
    __tablename__ = "booth_visits"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    booth_id = Column(String, nullable=False)

class Survey(Base):
    __tablename__ = "surveys"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)

class SurveyResponse(Base):
    __tablename__ = "survey_responses"
    id = Column(String, primary_key=True, index=True)
    survey_id = Column(String, ForeignKey("surveys.id"))
    user_id = Column(String, nullable=False)
    answer = Column(Text)

    survey = relationship("Survey", backref="responses")
