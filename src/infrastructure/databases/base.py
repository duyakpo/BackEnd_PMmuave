<<<<<<< HEAD

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mssql+pymssql://sa:Aa123456@127.0.0.1:1433/FlaskApiDB"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # Hợp lệ cho mọi version SQLAlchemy

# Kết nối SQL Server
DATABASE_URL = "mssql+pymssql://sa:Aa123456@127.0.0.1:1433/FlaskApiDB"

# Tạo engine
engine = create_engine(DATABASE_URL, echo=True)

# Tạo session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base cho các model kế thừa
Base = declarative_base()
>>>>>>> master
