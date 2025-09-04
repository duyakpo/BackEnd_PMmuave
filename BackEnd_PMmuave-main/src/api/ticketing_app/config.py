# config.py
class Config:
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///ticketing.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
