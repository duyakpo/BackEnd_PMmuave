from infrastructure.databases.mssql import init_mssql
from infrastructure.models import todo_model, user, event, survey, sponor, sponor_event, ticket, survey_response, ticket_type, invoice, invoice_line

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base
