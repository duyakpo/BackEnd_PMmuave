# models.py - ORM models cho các bảng: hoa_don, dong_hoa_don, ve

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class HoaDon(Base):
    __tablename__ = "hoa_don"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    tong_tien = Column(Float, default=0)

    # Quan hệ 1-nhiều với DongHoaDon
    chi_tiet = relationship("DongHoaDon", back_populates="hoa_don")


class DongHoaDon(Base):
    __tablename__ = "dong_hoa_don"

    id = Column(Integer, primary_key=True, index=True)
    hoa_don_id = Column(Integer, ForeignKey("hoa_don.id"))
    ve_id = Column(Integer, ForeignKey("ve.id"))
    so_luong = Column(Integer, default=1)

    # Quan hệ
    hoa_don = relationship("HoaDon", back_populates="chi_tiet")
    ve = relationship("Ve", back_populates="dong_hoa_don")


class Ve(Base):
    __tablename__ = "ve"

    id = Column(Integer, primary_key=True, index=True)
    ten_su_kien = Column(String, index=True)
    gia = Column(Float)
    qr_code = Column(String, nullable=True)  # link ảnh QR code hoặc chuỗi base64

    # Quan hệ
    dong_hoa_don = relationship("DongHoaDon", back_populates="ve")
