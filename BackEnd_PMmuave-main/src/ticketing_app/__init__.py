# ticketing_app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from ticketing_app.infrastructure.databases import db, init_db

migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Config
    app.config["SECRET_KEY"] = "your_secret_key_here"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticketing.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_here"

    # Gắn extension
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Khởi tạo DB
    init_db(app)

    # Route test
    @app.route("/")
    def home():
        return "Server running OK"

    return app
