from flask import Blueprint, request, jsonify
from src.services.survey_service import SurveyService
from src.api.schemas.survey import SurveySchema

survey_bp = Blueprint("surveys", _name_)
service = SurveyService()
schema = SurveySchema()

@survey_bp.route("/events/<int:event_id>/surveys", methods=["POST"])
def create_survey(event_id):
    data = request.json
    errors = schema.validate({**data, "event_id": event_id})
    if errors:
        return jsonify(errors), 400
    survey = service.create(event_id, data["title"])
    return schema.dump(survey), 201