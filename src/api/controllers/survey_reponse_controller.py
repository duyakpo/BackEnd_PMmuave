from flask import Blueprint, request, jsonify
from api.schemas.survey_reponse_schema import SurveyResponseRequestSchema, SurveyResponseResponseSchema
from infrastructure.services.survey_reponse_service import SurveyResponseService

bp = Blueprint("survey_response", __name__, url_prefix="/api/survey_responses")

service = SurveyResponseService()
req_schema = SurveyResponseRequestSchema()
res_schema = SurveyResponseResponseSchema()

@bp.route("", methods=["POST"])
def create_survey_response():
    """
    Submit survey response
    ---
    post:
      summary: Create a survey response
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SurveyResponseRequest'
      responses:
        201:
          description: Survey response created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SurveyResponseResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = req_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    sr = service.create_response(data)
    return jsonify(res_schema.dump(sr)), 201

@bp.route("", methods=["GET"])
def list_survey_responses():
    """
    List all survey responses
    ---
    get:
      summary: Get all survey responses
      responses:
        200:
          description: List of survey responses
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SurveyResponseResponse'
    """
    responses = service.list_responses()
    return jsonify(res_schema.dump(responses, many=True)), 200
