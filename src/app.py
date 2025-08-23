from flask import Flask, jsonify
from api.swagger import spec
from api.controllers.user_controller import bp as user_bp
from api.controllers.ticket_controller import bp as ticket_bp
from api.controllers.sponsor_controller import bp as sponsor_bp
from api.controllers.sponsor_visit_controller import bp as sponsor_visit_bp
from api.controllers.survey_controller import bp as survey_bp
from api.controllers.survey_reponse_controller import bp as survey_response_bp
from api.controllers.event_controller import bp as event_bp
from api.controllers.checkin_controller import bp as checkin_bp

from api.middleware import middleware
from infrastructure.databases import init_db
from config import Config
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo Swagger
    Swagger(app)

    # Đăng ký các blueprint
    app.register_blueprint(user_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(checkin_bp)
    app.register_blueprint(sponsor_bp)
    app.register_blueprint(sponsor_visit_bp)
    app.register_blueprint(survey_bp)
    app.register_blueprint(survey_response_bp)

    # Thêm Swagger UI
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Flask Clean Architecture API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Khởi tạo database
    try:
        init_db(app)
    except Exception as e:
        print(f"Error initializing database: {e}")

    # Đăng ký middleware
    middleware(app)

    # Đăng ký tất cả các route cho Swagger
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            view_func = app.view_functions[rule.endpoint]
            try:
                spec.path(view=view_func)
            except Exception:
                # Bỏ qua những route không thể thêm vào Swagger
                pass

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)
