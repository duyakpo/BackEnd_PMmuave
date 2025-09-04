def create_order(db: Session, user_id: int, order_data: schemas.OrderCreate):
    order = models.HoaDon(user_id=user_id)
    db.add(order)
    db.flush()  # để order.id có sẵn

    dong_list = [
        models.DongHoaDon(
            hoa_don_id=order.id,
            seat_number=item.seat_number,
            price=item.price
        )
        for item in order_data.items
    ]
    db.add_all(dong_list)

    ve_list = [
        models.Ve(
            hoa_don_id=order.id,
            qr_code=generate_qr_code(f"ORDER-{order.id}-SEAT-{item.seat_number}")
        )
        for item in order_data.items
    ]
    db.add_all(ve_list)

    db.commit()
    db.refresh(order)
    return order
