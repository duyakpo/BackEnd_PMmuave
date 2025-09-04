from marshmallow import Schema, fields

class SurveySchema(Schema):
    survey_id = fields.Int(dump_only=True)
    event_id = fields.Int(required=True)
    title = fields.Str(required=True)