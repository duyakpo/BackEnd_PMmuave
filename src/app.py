# src/app.py

from flask import Flask, jsonify
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint

from config import DevelopmentConfig  
from infrastructure.databases.mssql import create_tables 
from api.controllers.account_controller import bp as account_bp
from api.middleware import middleware
from api.swagger import spec


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

   
    app.config.from_object(config_class)
    
    Swagger(app)

    # Đăng ký blueprint 
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

    
    try:
        with app.app_context():
            create_tables()
        print("✅ Tables created successfully (if they didn't exist).")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

    # Middleware 
    middleware(app)

    # Quét routes cho Swagger 
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