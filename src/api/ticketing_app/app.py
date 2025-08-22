from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cấu hình database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/db_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo database với Flask app
    db.init_app(app)

    # Import blueprint
    from ticketing_app.routes import ticketing_bp
    app.register_blueprint(ticketing_bp, url_prefix='/ticketing')

    return app

# Chạy app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
