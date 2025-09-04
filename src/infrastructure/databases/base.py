<<<<<<< HEAD

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mssql+pymssql://sa:Aa123456@127.0.0.1:1433/FlaskApiDB"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
=======
from sqlalchemy.orm import declarative_base

>>>>>>> dfa820c (initial commit: add backend code)
Base = declarative_base()