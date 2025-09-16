from flask import Blueprint, jsonify

def register_routes(app):
    bp = Blueprint("api", __name__)

    @bp.route("/hello", methods=["GET"])
    def hello():
        return jsonify({"message": "Hello from Ticketing API!"})

    app.register_blueprint(bp, url_prefix="/api")
