# src/api/schemas/user_schema.py
from marshmallow import Schema, fields

class UserRequestSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    role = fields.String(required=True)
    qr_code = fields.String()

class UserResponseSchema(Schema):
    id = fields.Int()
    name = fields.String()
    email = fields.String()
    role = fields.String()
    qr_code = fields.String()
