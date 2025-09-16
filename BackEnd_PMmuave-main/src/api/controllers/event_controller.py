# src/api/controllers/event_controller.py

from flask import Blueprint, jsonify, request
from src.infrastructure.databases.mssql import get_db
from src.infrastructure.repositories.event_repository import EventRepository
from src.infrastructure.repositories.ticket_type_repository import TicketTypeRepository
from src.infrastructure.models.event_model import Event
from src.infrastructure.models.sponsor_model import SponsorModel
from src.infrastructure.models.ticket_type_model import TicketTypeModel
from datetime import datetime

bp = Blueprint('event', __name__, url_prefix='/api/events')

# --------------------------
# Helpers
# --------------------------
def success_response(message, data=None, status=200):
    return jsonify({"success": True, "message": message, "data": data}), status

def error_response(message, status=400):
    return jsonify({"success": False, "message": message}), status

# --------------------------
# API cho Sự kiện (Events)
# --------------------------

@bp.route('/', methods=['GET'])
def list_events():
    """Lấy danh sách tất cả sự kiện."""
    db = next(get_db())
    try:
        repo = EventRepository(session=db)
        events = repo.list_all()
        results = [{"id": e.id, "ten_su_kien": e.ten_su_kien, "dia_diem": e.dia_diem} for e in events]
        return success_response("Danh sách sự kiện", results)
    finally:
        db.close()

@bp.route('/<int:event_id>', methods=['GET'])
def get_event_detail(event_id):
    """Lấy chi tiết một sự kiện."""
    db = next(get_db())
    try:
        repo = EventRepository(session=db)
        event = repo.find_by_id(event_id)
        if not event:
            return error_response("Event not found", 404)
        return success_response("Chi tiết sự kiện", {
            "id": event.id, 
            "ten_su_kien": event.ten_su_kien, 
            "mo_ta": event.mo_ta,
            "dia_diem": event.dia_diem
        })
    finally:
        db.close()

@bp.route('/', methods=['POST'])
def create_event():
    """(Operator) Tạo một sự kiện mới."""
    data = request.get_json()
    if not data or 'ten_su_kien' not in data:
        return error_response("Missing required field: ten_su_kien")

    db = next(get_db())
    try:
        repo = EventRepository(session=db)
        new_event = Event(
            ten_su_kien=data.get('ten_su_kien'),
            dia_diem=data.get('dia_diem'),
            mo_ta=data.get('mo_ta'),
            thoi_gian_bat_dau=datetime.utcnow()
        )
        created_event = repo.create(new_event)
        return success_response("Tạo sự kiện thành công", {
            "id": created_event.id, 
            "ten_su_kien": created_event.ten_su_kien
        }, 201)
    except Exception as e:
        db.rollback()
        return error_response(f"Database error: {str(e)}", 500)
    finally:
        db.close()

@bp.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """(Operator) Cập nhật một sự kiện."""
    data = request.get_json()
    db = next(get_db())
    try:
        repo = EventRepository(session=db)
        updated_event = repo.update(event_id, data)
        if not updated_event:
            return error_response("Event not found", 404)
        return success_response("Cập nhật thành công", {
            "id": updated_event.id, 
            "ten_su_kien": updated_event.ten_su_kien
        })
    except Exception as e:
        db.rollback()
        return error_response(f"Database error: {str(e)}", 500)
    finally:
        db.close()

# --------------------------
# API cho Loại vé (Ticket Types)
# --------------------------

@bp.route('/<int:event_id>/ticket-types', methods=['GET'])
def get_ticket_types(event_id):
    """Lấy danh sách các loại vé của một sự kiện."""
    db = next(get_db())
    try:
        repo = TicketTypeRepository(session=db)
        ticket_types = repo.list_for_event(event_id)
        results = [{"id": tt.id, "name": tt.name, "price": tt.price, "quantity": tt.quantity} for tt in ticket_types]
        return success_response("Danh sách loại vé", results)
    finally:
        db.close()

@bp.route('/<int:event_id>/ticket-types', methods=['POST'])
def create_ticket_type_for_event(event_id):
    """(Operator) Tạo loại vé mới cho sự kiện."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data or 'quantity' not in data:
        return error_response("Missing required fields")

    db = next(get_db())
    try:
        repo = TicketTypeRepository(session=db)
        new_ticket_type = TicketTypeModel(
            name=data.get('name'),
            price=data.get('price'),
            quantity=data.get('quantity'),
            event_id=event_id
        )
        created_ticket_type = repo.add_to_event(new_ticket_type)
        return success_response("Tạo loại vé thành công", {
            "id": created_ticket_type.id, 
            "name": created_ticket_type.name
        }, 201)
    except Exception as e:
        db.rollback()
        return error_response(f"Database error: {str(e)}", 500)
    finally:
        db.close()

# --------------------------
# API cho Nhà tài trợ (Sponsors)
# --------------------------

@bp.route('/<int:event_id>/sponsors', methods=['GET'])
def get_sponsors_for_event(event_id):
    """Lấy danh sách nhà tài trợ của một sự kiện."""
    db = next(get_db())
    try:
        repo = EventRepository(session=db)
        sponsors = repo.list_sponsors_for_event(event_id)
        results = [{"id": s.id, "company_name": s.company_name} for s in sponsors]
        return success_response("Danh sách nhà tài trợ", results)
    finally:
        db.close()

@bp.route('/<int:event_id>/sponsors', methods=['POST'])
def add_sponsor_to_event(event_id):
    """(Operator) Thêm nhà tài trợ vào sự kiện."""
    data = request.get_json()
    if not data or 'account_id' not in data or 'company_name' not in data:
        return error_response("Missing required fields")

    db = next(get_db())
    try:
        repo = EventRepository(session=db)
        new_sponsor = SponsorModel(
            account_id=data.get('account_id'),
            company_name=data.get('company_name'),
            booth_location=data.get('booth_location'),
            event_id=event_id 
        )
        created_sponsor = repo.add_sponsor_to_event(new_sponsor)
        return success_response("Thêm nhà tài trợ thành công", {
            "id": created_sponsor.id, 
            "company_name": created_sponsor.company_name
        }, 201)
    except Exception as e:
        db.rollback()
        return error_response(f"Database error: {str(e)}", 500)
    finally:
        db.close()
