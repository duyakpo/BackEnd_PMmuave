# runapp.py
from flask import Flask
from .database import db
from .routes import ticketing_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("ticketting_app.config.Config")

    db.init_app(app)

    # Tạo bảng (nếu chưa có)
    with app.app_context():
        db.create_all()

    # Register blueprint
    app.register_blueprint(ticketing_bp, url_prefix="/ticketing")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
