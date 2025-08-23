# api/schemas/sponsor_schema.py
from marshmallow import Schema, fields

class SponsorRequestSchema(Schema):
    name = fields.Str(required=True)
    contact_email = fields.Email(required=False)
    event_id = fields.Int(required=True)
# ID of the event this sponsor is associated with

class SponsorResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    contact_email = fields.Str()
    event_id = fields.Int()
