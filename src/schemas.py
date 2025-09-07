from marshmallow import Schema, fields

class CheckinSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    event_id = fields.Str(required=True)

class BoothVisitSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    booth_id = fields.Str(required=True)

class SurveySchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()

class SurveyResponseSchema(Schema):
    id = fields.Str(dump_only=True)
    survey_id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    answer = fields.Str(required=True)
