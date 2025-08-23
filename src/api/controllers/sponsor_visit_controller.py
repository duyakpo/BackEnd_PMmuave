from flask import Blueprint, request, jsonify
from api.schemas.sponsor_visit_shema import SponsorVisitRequestSchema, SponsorVisitResponseSchema
from infrastructure.services.sponsor_visit_service import SponsorVisitService

bp = Blueprint("sponsor_visit", __name__, url_prefix="/api/sponsor_visits")

service = SponsorVisitService()
req_schema = SponsorVisitRequestSchema()
res_schema = SponsorVisitResponseSchema()

@bp.route("", methods=["POST"])
def create_visit():
    """
    Save a sponsor visit (QR scan)
    ---
    post:
      summary: Record a user visiting a sponsor
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SponsorVisitRequest'
      responses:
        201:
          description: Visit recorded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SponsorVisitResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = req_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    visit = service.create_visit(data)
    return jsonify(res_schema.dump(visit)), 201

@bp.route("", methods=["GET"])
def list_visits():
    """
    List all sponsor visits
    ---
    get:
      summary: Get all sponsor visits
      responses:
        200:
          description: List of visits
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SponsorVisitResponse'
    """
    visits = service.list_visits()
    return jsonify(res_schema.dump(visits, many=True)), 200
