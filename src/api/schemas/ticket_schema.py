from marshmallow import Schema, fields

class TicketRequestSchema(Schema):
    event_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    type = fields.Str(required=True)
    status = fields.Str(load_default="unpaid")  # thay 'missing' bằng 'load_default'

class TicketResponseSchema(Schema):
    id = fields.Int()
    event_id = fields.Int()
    user_id = fields.Int()
    type = fields.Str()
    status = fields.Str()





