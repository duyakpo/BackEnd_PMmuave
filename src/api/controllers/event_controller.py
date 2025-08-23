# src/api/controllers/event_controller.py
from flask import Blueprint, request, jsonify
from api.schemas.event_schema import EventRequestSchema, EventResponseSchema
from infrastructure.services.event_service import EventService

bp = Blueprint("event", __name__, url_prefix="/api")

event_service = EventService()
request_schema = EventRequestSchema()
response_schema = EventResponseSchema()

@bp.route("/events", methods=["POST"])
def create_event():
    """
    Create a new event
    ---
    post:
      summary: Create event
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EventRequest'
      responses:
        201:
          description: Event created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    event = event_service.create_event(data)
    return jsonify(response_schema.dump(event)), 201

@bp.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    """
    Get event by id
    ---
    get:
      summary: Get event
      parameters:
        - name: event_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Event found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventResponse'
        404:
          description: Event not found
    """
    event = event_service.get_event(event_id)
    if not event:
        return jsonify({"message": "Event not found"}), 404
    return jsonify(response_schema.dump(event)), 200

@bp.route("/events", methods=["GET"])
def list_events():
    """
    List all events
    ---
    get:
      summary: List events
      responses:
        200:
          description: List of events
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/EventResponse'
    """
    events = event_service.list_events()
    return jsonify(response_schema.dump(events, many=True)), 200
