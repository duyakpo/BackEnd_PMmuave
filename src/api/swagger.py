# api/swagger.py
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from api.schemas.user_schema import UserRequestSchema, UserResponseSchema
from api.schemas.event_schema import EventRequestSchema, EventResponseSchema
from api.schemas.ticket_schema import TicketRequestSchema, TicketResponseSchema
from api.schemas.checkin_schema import CheckInRequestSchema, CheckInResponseSchema
from api.schemas.sponsor_schema import SponsorRequestSchema, SponsorResponseSchema
from api.schemas.sponsor_visit_shema import SponsorVisitRequestSchema, SponsorVisitResponseSchema
from api.schemas.survey_schema import SurveyRequestSchema, SurveyResponseSchema
from api.schemas.survey_reponse_schema import SurveyResponseRequestSchema, SurveyResponseResponseSchema

spec = APISpec(
    title="Event Management API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Thêm các schema
spec.components.schema("UserRequest", schema=UserRequestSchema)
spec.components.schema("UserResponse", schema=UserResponseSchema)
spec.components.schema("EventRequest", schema=EventRequestSchema)
spec.components.schema("EventResponse", schema=EventResponseSchema)
spec.components.schema("TicketRequest", schema=TicketRequestSchema)
spec.components.schema("TicketResponse", schema=TicketResponseSchema)
spec.components.schema("CheckinRequest", schema= CheckInRequestSchema)
spec.components.schema("CheckinResponse", schema= CheckInResponseSchema)
spec.components.schema("SponsorRequest", schema=SponsorRequestSchema)
spec.components.schema("SponsorResponse", schema=SponsorResponseSchema)
spec.components.schema("SponsorVisitRequest", schema=SponsorVisitRequestSchema)
spec.components.schema("SponsorVisitResponse", schema=SponsorVisitResponseSchema)
spec.components.schema("SurveyRequest", schema=SurveyRequestSchema)
spec.components.schema("SurveyResponse", schema=SurveyResponseSchema)
spec.components.schema("SurveyResponseRequest", schema=SurveyResponseRequestSchema)
spec.components.schema("SurveyResponseResponse", schema=SurveyResponseResponseSchema)
