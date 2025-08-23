# src/api/schemas/event_schema.py
from marshmallow import Schema, fields

class EventRequestSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str()
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    organizer_id = fields.Int(required=True)

class EventResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    organizer_id = fields.Int()
