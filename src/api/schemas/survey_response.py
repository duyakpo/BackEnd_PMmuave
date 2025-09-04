from marshmallow import Schema, fields

class SurveyResponseSchema(Schema):
    response_id = fields.Int(dump_only=True)
    survey_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    answer = fields.Str(required=True)
    