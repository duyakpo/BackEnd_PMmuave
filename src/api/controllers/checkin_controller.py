from flask import Blueprint, request, jsonify
from src.services.checkin_service import CheckinService
from src.api.schemas.checkin import CheckinSchema

checkin_bp = Blueprint("checkin", __name__)
service = CheckinService()
schema = CheckinSchema()

@checkin_bp.route("/checkin", methods=["POST"])
def create_checkin():
    data = request.json
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    checkin = service.create(data["user_id"], data["event_id"])
    return schema.dump(checkin), 201