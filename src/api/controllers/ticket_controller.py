from flask import Blueprint, request, jsonify
from api.schemas.ticket_schema import TicketRequestSchema, TicketResponseSchema
from infrastructure.services.ticket_service import TicketService

bp = Blueprint("ticket", __name__, url_prefix="/api")

ticket_service = TicketService()
req_schema = TicketRequestSchema()
res_schema = TicketResponseSchema()

@bp.route("/tickets", methods=["POST"])
def create_ticket():
    """
    Create a new ticket
    ---
    post:
      summary: Create ticket
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TicketRequest'
      responses:
        201:
          description: Ticket created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TicketResponse'
        400:
          description: Invalid input or user/event not found
    """
    data = request.get_json()
    errors = req_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    try:
        ticket = ticket_service.create_ticket(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(res_schema.dump(ticket)), 201

@bp.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ticket = ticket_service.get_ticket(ticket_id)
    if not ticket:
        return jsonify({"message": "Ticket not found"}), 404
    return jsonify(res_schema.dump(ticket)), 200

@bp.route("/tickets", methods=["GET"])
def list_tickets():
    tickets = ticket_service.list_tickets()
    return jsonify(res_schema.dump(tickets, many=True)), 200
