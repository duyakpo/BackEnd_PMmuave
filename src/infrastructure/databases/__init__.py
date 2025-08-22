from infrastructure.databases.mssql import init_mssql
from infrastructure.models import accounts_model, invoice_line_model, invoice_model, survey_model, survey_response_model, ticket_model, ticket_type_model,  event_model, sponsor_model, checkin_model, booth_visit_model

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base
