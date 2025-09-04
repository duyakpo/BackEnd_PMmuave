from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
<<<<<<< HEAD
from api.schemas.account_schema import AccountRequestSchema, AccountResponseSchema, AccountRoleUpdateSchema

spec = APISpec(
    title="Account API",
=======
from api.schemas.todo import TodoRequestSchema, TodoResponseSchema

spec = APISpec(
    title="Todo API",
>>>>>>> dfa820c (initial commit: add backend code)
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

<<<<<<< HEAD
# Thêm schema
spec.components.schema("AccountRequest", schema=AccountRequestSchema)
spec.components.schema("AccountResponse", schema=AccountResponseSchema)
spec.components.schema("AccountRoleUpdate", schema=AccountRoleUpdateSchema)

=======
# Đăng ký schema để tự động sinh model
spec.components.schema("TodoRequest", schema=TodoRequestSchema)
spec.components.schema("TodoResponse", schema=TodoResponseSchema)
>>>>>>> dfa820c (initial commit: add backend code)
