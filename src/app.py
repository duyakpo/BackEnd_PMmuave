from flask import Flask, jsonify
from api.controllers.account_controller import bp as account_bp
from api.middleware import middleware
from infrastructure.databases import init_db
from config import Config
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
from api.swagger import spec

def create_app():
    app = Flask(__name__)
    Swagger(app)

    # Register blueprint
    app.register_blueprint(account_bp)

    # Swagger UI
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Account API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Init DB
    try:
        init_db(app)
    except Exception as e:
        print(f"Error initializing database: {e}")

    # Middleware
    middleware(app)

    # Add routes to spec
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            view_func = app.view_functions[rule.endpoint]
            spec.path(view=view_func)

    # Swagger JSON
    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)


