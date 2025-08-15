from infrastructure.databases.mssql import init_mssql
from infrastructure.models import todo_model, user_model, event_model, survey, sponsor_model, sponor_event, ticket, survey_response, ticket_type, invoice, invoice_line, checkin_model, booth_visit_model

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base
