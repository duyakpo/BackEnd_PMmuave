from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from src.infrastructure.models.base import BaseModel

class User(BaseModel):
    __tablename__ = "user"

    id = Column("ma_user", Integer, primary_key=True, autoincrement=True)
    ho_ten = Column(String(100), nullable=False)
    so_dien_thoai = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(Enum("Guest", "Visitor", "Sponsor", "EventOperator", "CheckingStaff"), nullable=False)

    tickets = relationship("Ticket", back_populates="user")
    invoices = relationship("Invoice", back_populates="user")
    sponsorships = relationship("Sponsor", back_populates="user")
    checkins_made = relationship("Checkin", back_populates="staff", foreign_keys='Checkin.staff_id')
    booth_visits = relationship("BoothVisit", back_populates="visitor")
    survey_responses = relationship("SurveyResponse", back_populates="user")