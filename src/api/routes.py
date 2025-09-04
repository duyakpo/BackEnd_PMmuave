<<<<<<< HEAD
from src.api.controllers.account_controller import bp as account_bp

def register_routes(app):
    app.register_blueprint(account_bp)
=======
from src.api.controllers.checkin_controller import checkin_bp
from src.api.controllers.booth_visit_controller import booth_bp
from src.api.controllers.survey_controller import survey_bp
from src.api.controllers.survey_response_controller import response_bp

def init_routes(app):
    app.register_blueprint(checkin_bp, url_prefix="/api")
    app.register_blueprint(booth_bp, url_prefix="/api")
    app.register_blueprint(survey_bp, url_prefix="/api")
    app.register_blueprint(response_bp, url_prefix="/api")
>>>>>>> dfa820c (initial commit: add backend code)
