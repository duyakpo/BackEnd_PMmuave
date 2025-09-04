from marshmallow import Schema, fields

class BoothVisitSchema(Schema):
    visit_id = fields.Int(dump_only=True)
    sponsor_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    event_id = fields.Int(required=True)
    timestamp = fields.Datetime(dump_only=True)