from marshmallow import Schema, fields

class SurveyResponseRequestSchema(Schema):
    survey_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    response = fields.Str(required=True)

class SurveyResponseResponseSchema(Schema):
    id = fields.Int()
    survey_id = fields.Int()
    user_id = fields.Int()
    response = fields.Str()
