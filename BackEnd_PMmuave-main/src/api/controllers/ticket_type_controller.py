# src/api/controllers/ticket_type_controller.py

from flask import Blueprint, jsonify, request
from src.infrastructure.databases.mssql import get_db
from src.infrastructure.repositories.ticket_type_repository import TicketTypeRepository

bp = Blueprint('ticket_type', __name__, url_prefix='/api/ticket-types')

@bp.route('/<int:type_id>', methods=['PUT'])
def update_ticket_type(type_id):
    data = request.get_json()
    db = next(get_db())
    repo = TicketTypeRepository(session=db)
    updated = repo.update(type_id, data)
    if not updated:
        return jsonify({"message": "TicketType not found"}), 404
    return jsonify({"id": updated.id, "name": updated.name}), 200