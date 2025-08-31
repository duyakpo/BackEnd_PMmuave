from marshmallow import Schema, fields

class AccountRequestSchema(Schema):
    ma_user = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    vai_tro = fields.Str(required=False)

class AccountResponseSchema(Schema):
    id = fields.Int(required=True)
    ma_user = fields.Str(required=True)
    email = fields.Str(required=True)
    vai_tro = fields.Str(required=True)

class AccountRoleUpdateSchema(Schema):
    vai_tro = fields.Str(required=True)
