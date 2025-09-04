from .models import HoaDon, DongHoaDon, Ve, db
from .utils import generate_qr_code

def create_order(user_id: int, items: list):
    """
    items = [
        {"ten_ve": "VIP", "so_luong": 2, "don_gia": 150},
        {"ten_ve": "Standard", "so_luong": 1, "don_gia": 100},
    ]
    """
    # Tạo hóa đơn
    order = HoaDon(user_id=user_id)
    db.session.add(order)
    db.session.flush()  # để order.id có sẵn

    # Tạo chi tiết hóa đơn
    chi_tiet_list = []
    for item in items:
        dong = DongHoaDon(
            hoa_don_id=order.id,
            ten_ve=item["ten_ve"],
            so_luong=item["so_luong"],
            don_gia=item["don_gia"]
        )
        db.session.add(dong)
        chi_tiet_list.append(dong)

        # Tạo vé tương ứng
        for i in range(item["so_luong"]):
            ve = Ve(
                dong_hoa_don=dong,
                qr_code=generate_qr_code(f"ORDER-{order.id}-SEAT-{item['ten_ve']}-{i+1}")
            )
            db.session.add(ve)

    db.session.commit()
    db.session.refresh(order)
    return order
