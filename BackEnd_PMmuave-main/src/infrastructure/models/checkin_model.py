<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
class CheckinModel(Base):
    __tablename__ = "checkins"
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
=======
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
class CheckinModel(Base):
    __tablename__ = "checkins"
    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
>>>>>>> 76b11cf79d76e4d4a56d8a8e010d0ba49af93f46
    checkin_time = Column(DateTime, nullable=False)