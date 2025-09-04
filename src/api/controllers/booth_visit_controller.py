from flask import Blueprint, request, jsonify
from src.services.booth_visit_service import BoothVisitService
from src.api.schemas.booth_visit import BoothVisitSchema

booth_bp = Blueprint("booth_visits", _name_)
service = BoothVisitService()
schema = BoothVisitSchema()

@booth_bp.route("/booth-visits/scan", methods=["POST"])
def create_visit():
    data = request.json
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    visit = service.create(data["sponsor_id"], data["user_id"], data["event_id"])
    return schema.dump(visit), 201