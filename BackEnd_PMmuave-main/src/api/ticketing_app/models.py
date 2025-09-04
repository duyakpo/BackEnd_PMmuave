# models.py
from .database import db

class Ve(db.Model):
    __tablename__ = "ve"
    id = db.Column(db.Integer, primary_key=True)
    ten_ve = db.Column(db.String(100), nullable=False)
    gia = db.Column(db.Float, nullable=False)
    qr_code = db.Column(db.Text, nullable=True)

class HoaDon(db.Model):
    __tablename__ = "hoa_don"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    tong_tien = db.Column(db.Float, default=0.0)
    dong_hoa_dons = db.relationship("DongHoaDon", backref="hoa_don", lazy=True)

class DongHoaDon(db.Model):
    __tablename__ = "dong_hoa_don"
    id = db.Column(db.Integer, primary_key=True)
    hoa_don_id = db.Column(db.Integer, db.ForeignKey("hoa_don.id"), nullable=False)
    ve_id = db.Column(db.Integer, db.ForeignKey("ve.id"), nullable=False)
    so_luong = db.Column(db.Integer, nullable=False)
    don_gia = db.Column(db.Float, nullable=False)
