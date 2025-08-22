from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base
class SurveyResponseModel(Base):
    __tablename__ = "survey_responses"
    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    respondent_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text)
    rating = Column(Integer)
   
