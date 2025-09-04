from flask import Flask, jsonify
from ticketing_app.routes import ticketing_bp  # import ticketing blueprint
from api.controllers.account_controller import bp as account_bp
from api.middleware import middleware
from infrastructure.databases import init_db
from config import Config
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
from api.swagger import spec

def create_app():
    # Khởi tạo app Flask
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo Swagger
    Swagger(app)

    # Đăng ký blueprint
    app.register_blueprint(account_bp)
    app.register_blueprint(ticketing_bp)

    # Swagger UI
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_bp = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Account API + Ticketing API"}
    )
    app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)

    # Khởi tạo DB
    try:
        init_db(app)
    except Exception as e:
        print(f"Error initializing database: {e}")

    # Middleware
    middleware(app)

    # Thêm routes vào Swagger spec
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            view_func = app.view_functions[rule.endpoint]
            spec.path(view=view_func)

    # Route Swagger JSON
    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)
