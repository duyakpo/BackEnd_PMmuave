# ticketing_app/infrastructure/databases.py

from ticketing_app import db

def init_db(app):
    """Khởi tạo database trong Flask"""
    with app.app_context():
        db.create_all()
