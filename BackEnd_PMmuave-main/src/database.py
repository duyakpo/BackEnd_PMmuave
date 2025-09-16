# ticketing_app/infrastructure/databases.py
from flask_sqlalchemy import SQLAlchemy

# Khởi tạo db ở đây
db = SQLAlchemy()

def init_db(app):
    """Khởi tạo database trong Flask"""
    with app.app_context():
        db.create_all()
