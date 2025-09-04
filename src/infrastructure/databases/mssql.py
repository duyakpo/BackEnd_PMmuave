<<<<<<< HEAD
# src/infrastructure/databases/mssql.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from .base import Base

engine = create_engine(Config.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
  
    try:
        from infrastructure.models.todo_model import Todo 
        from infrastructure.models.accounts_model import Account
        from infrastructure.models.booth_visit_model import BoothVisit
        from infrastructure.models.checkin_model import Checkin
        from infrastructure.models.event_model import Event
        from infrastructure.models.invoice_model import Invoice
        from infrastructure.models.invoice_line_model import InvoiceLine
        from infrastructure.models.sponsor_model import Sponsor
        from infrastructure.models.survey_model import Survey
        from infrastructure.models.survey_response_model import SurveyResponse
        from infrastructure.models.ticket_model import Ticket
        from infrastructure.models.ticket_type_model import TicketType
        from infrastructure.models.user import User

    except ImportError as e:
        print(f"Lỗi import model: {e}")
        print("Vui lòng kiểm tra lại tên file và tên class trong các file model.")
        return

    Base.metadata.create_all(bind=engine)

def get_db():
    """Cung cấp một session cho mỗi request và đảm bảo nó được đóng lại."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from infrastructure.databases.base import Base

# Database configuration
DATABASE_URL = Config.DATABASE_URI
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
def init_mssql(app):
    Base.metadata.create_all(bind=engine)
>>>>>>> dfa820c (initial commit: add backend code)
