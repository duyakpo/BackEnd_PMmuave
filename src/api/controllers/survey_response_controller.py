from flask import Blueprint, request, jsonify
from src.services.survey_response_service import SurveyResponseService
from src.api.schemas.survey_response import SurveyResponseSchema

response_bp = Blueprint("survey_responses", _name_)
service = SurveyResponseService()
schema = SurveyResponseSchema()

@response_bp.route("/surveys/<int:survey_id>/responses", methods=["POST"])
def create_response(survey_id):
    data = request.json
    errors = schema.validate({**data, "survey_id": survey_id})
    if errors:
        return jsonify(errors), 400
    response = service.create(survey_id, data["user_id"], data["answer"])
    return schema.dump(response), 201

@response_bp.route("/surveys/<int:survey_id>/responses", methods=["GET"])
def get_responses(survey_id):
    responses = service.get_by_survey(survey_id)
    return jsonify(schema.dump(responses, many=True))