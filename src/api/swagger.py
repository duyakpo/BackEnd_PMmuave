from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from api.schemas.account_schema import AccountRequestSchema, AccountResponseSchema, AccountRoleUpdateSchema

spec = APISpec(
    title="Account API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Thêm schema
spec.components.schema("AccountRequest", schema=AccountRequestSchema)
spec.components.schema("AccountResponse", schema=AccountResponseSchema)
spec.components.schema("AccountRoleUpdate", schema=AccountRoleUpdateSchema)

