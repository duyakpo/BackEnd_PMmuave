from flask import Blueprint, jsonify

ticketing_bp = Blueprint("ticketing", __name__)

@ticketing_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Ticketing API!"})
