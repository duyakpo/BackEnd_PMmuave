from flask import Blueprint, request, jsonify
from api.schemas.checkin_schema import CheckInRequestSchema, CheckInResponseSchema
from infrastructure.services.checkin_service import CheckInService

bp = Blueprint("checkin", __name__, url_prefix="/api")

checkin_service = CheckInService()
req_schema = CheckInRequestSchema()
res_schema = CheckInResponseSchema()

@bp.route("/checkins", methods=["POST"])
def create_checkin():
    """
    Create a new check-in
    ---
    post:
      summary: Check-in a user for an event
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CheckInRequest'
      responses:
        201:
          description: Check-in created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckInResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = req_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    checkin = checkin_service.create_checkin(data)
    return jsonify(res_schema.dump(checkin)), 201

@bp.route("/checkins/<int:checkin_id>", methods=["GET"])
def get_checkin(checkin_id):
    checkin = checkin_service.get_checkin(checkin_id)
    if not checkin:
        return jsonify({"message": "Check-in not found"}), 404
    return jsonify(res_schema.dump(checkin)), 200

@bp.route("/checkins", methods=["GET"])
def list_checkins():
    checkins = checkin_service.list_checkins()
    return jsonify(res_schema.dump(checkins, many=True)), 200
