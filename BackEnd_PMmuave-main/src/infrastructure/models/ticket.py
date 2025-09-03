from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from src.infrastructure.models.base import BaseModel

class Ticket(BaseModel):
    __tablename__ = "ve"

    id = Column("ma_ve", Integer, primary_key=True, autoincrement=True)
    ma_loai_ve = Column(Integer, ForeignKey("loai_ve.ma_loai_ve"))
    ma_su_kien = Column(Integer, ForeignKey("su_kien.ma_su_kien"))
    ma_user = Column(Integer, ForeignKey("user.ma_user"))
    tinh_trang = Column(Enum("ChuaBan", "DaBan", "CheckIn"), default="ChuaBan")
    qr_code = Column(String(200))

ticket_type = relationship("TicketType", back_populates="tickets")

    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="tickets")

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tickets")

    checkin = relationship("Checkin", back_populates="ticket", uselist=False)
