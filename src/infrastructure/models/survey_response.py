from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from infrastructure.databases.base import Base
class SurveyResponseModel(Base):
    __tablename__ = 'survey_responses'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    answer = Column(Text)
    submitted_at = Column(DateTime)