from marshmallow import Schema, fields

class SponsorVisitRequestSchema(Schema):
    sponsor_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    event_id = fields.Int(required=True)
    visit_time = fields.DateTime(required=False)  # nếu không gửi thì backend sẽ set giờ hiện tại

class SponsorVisitResponseSchema(Schema):
    id = fields.Int()
    sponsor_id = fields.Int()
    user_id = fields.Int()
    event_id = fields.Int()
    visit_time = fields.DateTime()
