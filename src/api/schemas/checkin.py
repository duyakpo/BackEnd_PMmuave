from marshmallow import Schema, fields

class CheckinSchema(Schema):
    checkin_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    event_id = fields.Int(required=True)
    timestamp = fields.Datetime(dump_only=True)
    