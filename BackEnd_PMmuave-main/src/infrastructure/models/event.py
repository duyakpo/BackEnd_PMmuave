from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.infrastructure.models.base import BaseModel

class Event(BaseModel):
    __tablename__ = "su_kien"

    id = Column("ma_su_kien", Integer, primary_key=True, autoincrement=True)
    ten_su_kien = Column(String(200), nullable=False)
    loai_su_kien = Column(String(50))  # Seminar, Hội thảo...
    thoi_gian_bat_dau = Column(DateTime)
    thoi_gian_ket_thuc = Column(DateTime)
    dia_diem = Column(String(200))
    mo_ta = Column(Text)
    
    tickets = relationship("Ticket", back_populates="event")
