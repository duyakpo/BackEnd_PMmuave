from flask import request, jsonify
from .orders import create_order

@ticketing_bp.route("/orders", methods=["POST"])
def order_route():
    data = request.get_json()
    user_id = 1  # demo, lấy từ session/JWT trong production
    order = create_order(user_id, data["items"])
    return jsonify({"order_id": order.id, "status": order.status})
