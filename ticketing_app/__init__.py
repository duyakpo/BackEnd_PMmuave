from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "your_secret_key_here"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticketing.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_here"

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import models để Flask-Migrate nhận diện
    from ticketing_app import models  

    from ticketing_app.routes import ticketing_bp
    app.register_blueprint(ticketing_bp, url_prefix="/api")

    return app
