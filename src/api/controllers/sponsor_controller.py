# api/controllers/sponsor_controller.py
from flask import Blueprint, request, jsonify
from api.schemas.sponsor_schema import SponsorRequestSchema, SponsorResponseSchema
from infrastructure.services.sponsor_service import SponsorService

bp = Blueprint("sponsor", __name__, url_prefix="/api/sponsors")

service = SponsorService()
req_schema = SponsorRequestSchema()
res_schema = SponsorResponseSchema()


@bp.route("", methods=["POST"])
def create_sponsor():
    """
    Create a new sponsor
    ---
    post:
      summary: Add a new sponsor
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SponsorRequest'
      responses:
        201:
          description: Sponsor created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SponsorResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = req_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    sponsor = service.create_sponsor(data)
    return jsonify(res_schema.dump(sponsor)), 201


@bp.route("/<int:sponsor_id>", methods=["GET"])
def get_sponsor(sponsor_id):
    """
    Get a sponsor by ID
    ---
    get:
      summary: Retrieve a sponsor by ID
      parameters:
        - name: sponsor_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Sponsor details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SponsorResponse'
        404:
          description: Sponsor not found
    """
    sponsor = service.get_sponsor(sponsor_id)
    if not sponsor:
        return jsonify({"message": "Sponsor not found"}), 404
    return jsonify(res_schema.dump(sponsor)), 200


@bp.route("", methods=["GET"])
def list_sponsors():
    """
    List all sponsors
    ---
    get:
      summary: Get all sponsors
      responses:
        200:
          description: List of sponsors
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SponsorResponse'
    """
    sponsors = service.list_sponsors()
    return jsonify(res_schema.dump(sponsors, many=True)), 200

