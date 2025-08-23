from marshmallow import Schema, fields

class CheckInRequestSchema(Schema):
    user_id = fields.Int(required=True)
    event_id = fields.Int(required=True)
    time = fields.DateTime(required=False)  # Nếu không gửi thì có thể auto lấy giờ hiện tại

class CheckInResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    event_id = fields.Int()
    time = fields.DateTime()
