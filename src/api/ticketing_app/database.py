# database.py - Kết nối với cơ sở dữ liệu

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ở đây anh dùng SQLite cho đơn giản. Em có thể đổi sang MySQL/Postgres nếu cần.
DATABASE_URL = "sqlite:///./ticketing.db"

# Tạo engine kết nối
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # chỉ cần cho SQLite
)

# Tạo Session để thao tác DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class để định nghĩa ORM models
Base = declarative_base()

# Dependency cho FastAPI: lấy session và đóng sau khi dùng
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Tạo session toàn cục để các controller dùng
db_session = SessionLocal()
