from src.api.controllers.account_controller import bp as account_bp

def register_routes(app):
    app.register_blueprint(account_bp)
