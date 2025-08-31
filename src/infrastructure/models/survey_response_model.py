from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from infrastructure.databases.base import Base
class SurveyResponseModel(Base):
    __tablename__ = "survey_responses"
    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    respondent_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    content = Column(Text)
    rating = Column(Integer)
