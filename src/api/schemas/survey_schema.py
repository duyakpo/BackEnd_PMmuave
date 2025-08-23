from marshmallow import Schema, fields

class SurveyRequestSchema(Schema):
    event_id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=False)

class SurveyResponseSchema(Schema):
    id = fields.Int()
    event_id = fields.Int()
    title = fields.Str()
    description = fields.Str()
