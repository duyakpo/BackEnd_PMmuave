# routes.py
from flask import Blueprint, request, jsonify
from .database import db
from . import models
import qrcode, io, base64

ticketing_bp = Blueprint("ticketing_app", __name__)

# ===== Helper: Sinh QR code =====
def generate_qr_code(data: str) -> str:
    qr_img = qrcode.make(data)
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

# ========== API 1: Đặt vé ==========
@ticketing_bp.route("/orders", methods=["POST"])
def create_order():
    payload = request.json
    user_id = payload["user_id"]
    chi_tiet = payload["chi_tiet"]

    hoa_don = models.HoaDon(user_id=user_id, tong_tien=0.0)
    db.session.add(hoa_don)
    db.session.commit()

    tong_tien = 0
    for dong in chi_tiet:
        ve = models.Ve.query.get(dong["ve_id"])
        if not ve:
            return jsonify({"error": f"Vé {dong['ve_id']} không tồn tại"}), 404

        dong_hd = models.DongHoaDon(
            hoa_don_id=hoa_don.id,
            ve_id=ve.id,
            so_luong=dong["so_luong"],
            don_gia=ve.gia
        )
        db.session.add(dong_hd)

        # Cộng tiền
        tong_tien += ve.gia * dong["so_luong"]

        # Sinh QR code
        qr_data = f"TicketID:{ve.id}-User:{user_id}"
        ve.qr_code = generate_qr_code(qr_data)

    hoa_don.tong_tien = tong_tien
    db.session.commit()
    return jsonify({"hoa_don_id": hoa_don.id, "tong_tien": hoa_don.tong_tien})

# ========== API 2: Lấy danh sách vé ==========
@ticketing_bp.route("/me/tickets", methods=["GET"])
def get_my_tickets():
    user_id = request.args.get("user_id", type=int)
    tickets = (
        models.Ve.query
        .join(models.DongHoaDon)
        .join(models.HoaDon)
        .filter(models.HoaDon.user_id == user_id)
        .all()
    )
    result = []
    for v in tickets:
        result.append({
            "id": v.id,
            "ten_ve": v.ten_ve,
            "gia": v.gia,
            "qr_code": v.qr_code
        })
    return jsonify(result)

# ========== API 3: Lấy chi tiết 1 vé ==========
@ticketing_bp.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ve = models.Ve.query.get(ticket_id)
    if not ve:
        return jsonify({"error": "Vé không tồn tại"}), 404
    return jsonify({
        "id": ve.id,
        "ten_ve": ve.ten_ve,
        "gia": ve.gia,
        "qr_code": ve.qr_code
    })

# ========== API 4: Lịch sử hóa đơn ==========
@ticketing_bp.route("/me/orders", methods=["GET"])
def get_my_orders():
    user_id = request.args.get("user_id", type=int)
    orders = models.HoaDon.query.filter_by(user_id=user_id).all()
    result = []
    for o in orders:
        result.append({
            "id": o.id,
            "user_id": o.user_id,
            "tong_tien": o.tong_tien
        })
    return jsonify(result)
