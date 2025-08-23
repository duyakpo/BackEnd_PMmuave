# api/routes.py
from flask import Blueprint, jsonify
from api.controllers.user_controller import bp as user_bp
from api.controllers.event_controller import bp as event_bp
from api.controllers.ticket_controller import bp as ticket_bp
from api.controllers.checkin_controller import bp as checkin_bp
from api.controllers.sponsor_controller import bp as sponsor_bp
from api.controllers.sponsor_visit_controller import bp as sponsor_visit_bp
from api.controllers.survey_controller import bp as survey_bp
from api.controllers.survey_reponse_controller import bp as survey_response_bp

def register_routes(app):
    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(checkin_bp)
    app.register_blueprint(sponsor_bp)
    app.register_blueprint(sponsor_visit_bp)
    app.register_blueprint(survey_bp)
    app.register_blueprint(survey_response_bp)

