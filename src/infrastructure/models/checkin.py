from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
# 9. CHECKIN
class CheckinModel(Base):
    __tablename__ = 'checkins'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'), nullable=False)
    checkin_time = Column(DateTime, nullable=False)
    staff_id = Column(Integer, ForeignKey('users.id'))