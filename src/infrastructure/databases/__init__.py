from infrastructure.databases.mssql import init_mssql
from infrastructure.models import user_model, event_model, ticket_model, checkin_model, sponsor_model, sponsor_visit_model, survey_model, survey_response_model

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base