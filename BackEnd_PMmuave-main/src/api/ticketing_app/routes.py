# routes.py - Định nghĩa API mua vé và quản lý vé

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, models
import qrcode
import io
import base64

router = APIRouter()

# ========== API 1: Đặt vé ==========
@router.post("/orders")
def create_order(user_id: int, ve_id: int, so_luong: int, db: Session = Depends(database.get_db)):
    # Tìm vé trong DB
    ve = db.query(models.Ve).filter(models.Ve.id == ve_id).first()
    if not ve:
        raise HTTPException(status_code=404, detail="Vé không tồn tại")

    # Tạo hóa đơn
    hoa_don = models.HoaDon(user_id=user_id, tong_tien=ve.gia * so_luong)
    db.add(hoa_don)
    db.commit()
    db.refresh(hoa_don)

    # Tạo chi tiết hóa đơn
    dong_hd = models.DongHoaDon(hoa_don_id=hoa_don.id, ve_id=ve.id, so_luong=so_luong)
    db.add(dong_hd)

    # Sinh QR code cho vé
    qr_data = f"TicketID:{ve.id}-User:{user_id}"
    qr_img = qrcode.make(qr_data)
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    qr_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    ve.qr_code = qr_base64

    db.commit()
    return {"order_id": hoa_don.id, "qr_code": ve.qr_code}


# ========== API 2: Lấy danh sách vé ==========
@router.get("/me/tickets")
def get_my_tickets(user_id: int, db: Session = Depends(database.get_db)):
    tickets = (
        db.query(models.Ve)
        .join(models.DongHoaDon)
        .join(models.HoaDon)
        .filter(models.HoaDon.user_id == user_id)
        .all()
    )
    return tickets


# ========== API 3: Lấy chi tiết 1 vé ==========
@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(database.get_db)):
    ve = db.query(models.Ve).filter(models.Ve.id == ticket_id).first()
    if not ve:
        raise HTTPException(status_code=404, detail="Vé không tồn tại")
    return ve


# ========== API 4: Lịch sử hóa đơn ==========
@router.get("/me/orders")
def get_my_orders(user_id: int, db: Session = Depends(database.get_db)):
    orders = db.query(models.HoaDon).filter(models.HoaDon.user_id == user_id).all()
    return orders
